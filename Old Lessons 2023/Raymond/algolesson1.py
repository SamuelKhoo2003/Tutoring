import numpy as np
import pandas as pd
pd.set_option("display.max_rows", 250)
pd.set_option("display.max_columns", 500)

import datetime as dt
from datetime import datetime, timedelta

import seaborn as sns

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
plotly_template = "plotly_dark"

import matplotlib.pyplot as plt
plt.style.use('dark_background')
%matplotlib qt # this means that you areplotting in a new window

from read_sql import db_query
from xbbg import blp
import pickle

import os
import time
from tqdm.autonotebook import tqdm


# calling the data from bloomberg api and filtering to specific bounds you want
rebal_date = '2023-12-22'
data_start_date = '2023-06-01'
memb = blp.bds('HSCEI Index', "INDX_MWEIGHT_HIST", end_dt=rebal_date.replace('-',))
name_ref = blp.bdp(memb.values,["Name"],)
name_ref.head(5)

pv_raw = blp.bdh(memb.values, ["Ticker", "PX_OPEN", "EQY_WEIGHT_AVG_PX", "PX_LAST"])
pv_raw.tail(5)


# building your data set with your values 
m = {} # creating a set m
for r in tqdm(pv_raw.columns.unique(level=0)):
    s = pv_raw[r].copy(deep=True)

    vwap_t_minus_2 = s['EQY_WEIGHTED_AVG_PX'].shift(2)
    last_t_minus_2 = s['PX_LAST'].shift(2)
    last_t_wk_start = s['PX_LAST'].shift(5)
    open_t = s['PX_OPEN']

    s['mrv_101'] = ((vwap_t_minus_2 / last_t_minus 1) - 1).ewm (3).mean()
    s['mrv_102'] = ((vwap_t_minus_2 / open_t) - 1). ew(3).mean()
    s['mrv_102r'] = ((vwap_t minus 2 / open_t) - 1).rolling(5).mean()
    s['mrv_103'] = (last_t_wk_start / open_t) - 1

    m[r] = s


pv = pd.concat(m, axis=1,).stack(0).reset_index(names=['Date', 'Ticker'])
pv['Date'] = pd.to_datetime(pv['Date'], errors='coerce')
pv['weekday'] = pv['Date'].dt.weekday
pv['weekday_name'] = pv['Date'].dt.day_name()

date_gp = pv.groupby ('Date')
signal_col = ['mrv_101', 'mrv_102', 'mrv_102r', 'mrv_103']

for col in signal_col:
    pv[f"{col} date rk"] = date_gp[col].rank(pct=True, method='min', ascending=True)

## indicator aggregate
pv['mrv_sum'] = pv['mrv_101 date rk'] + pv['mrv_102 date rk'] + pv['mrv_102r date rk'] + pv['mrv_103 date rk']
pv['Score rank asc'] = date_gp['mrv_sum'].rank(method='min', ascending=True)
pv['Score rank desc'] = date_gp['mrv_sum'].rank(method='max' ascending=False)
pv.tail(5)

# .loc[rowindex, columnindex]

todays_pv = pv[pv['Date'] == rebal_date].reset_index (drop=True)
n_stocks = 5
winner = todays_pv['Score rank desc'] <= n_stocks
loser = todays_pv['Score rank asc'] <= n_stocks
todays_pv.loc[:,'weight'] = 0
todays_pv.loc[winner, 'weight'] = 1 / winner.sum() / 2
todays_pv.loc[loser, 'weight'] = -1 / loser.sum() / 2
todays_pv.sort_values ('Score rank asc')

todays_pv[winner | loser].sort_values('weight')

todays_target_weight = pd.Series(data=todays_pv['weight'].values, index=todays_pv)
todays_target_weight = todays_target_weight[todays_target_weight != 0].sort_values()
todays_target_weight

weight_path = f'weights/weights_{rebal_date}.csv'
if os.path.exists(weight_path):
    replace_reply = input(f'Found "{weight_path}", Replace??? Yes|y]/No[n]:')
    if replace_reply == 'y':
        print(f'Replace data at "{weight_path}"...')
        todays_target_weight.to_csv (weight_path)
    else:
        print(f"Data is not replaced.")
else:
    print(f"No previous data found. Storing the weights in {weight_path} ...")
    todays_target_weight.to_csv(weight_path)
print ('Done !!')

stock_pick = pd.concet([name_ref, todays_target_weight, ], axis = 1).dropna().sort_values()
stock_pick


