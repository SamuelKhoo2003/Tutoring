# 2nd lesson

all_stock = xsdf.copy(deep=True)

all_stock['mrv indicator'] = all_stock["mrv_101 {'w': 3} date rk"] + all_stock["mrv_102 {'w': 3} date rk"] + all_stock["mrv_102r {'w': 3} date rk"] + all_stock["mrv_103 {'w': 3} date rk"]
all_stock['senti indicator'] = all_stock["ss_pct {'w': 2} date rk"] + all_stock["sb_ch {'w': 5} date rk"] + all_stock["target_px_ch {'d': 20} date rk"] + all_stock["rating_ch {'d': 20} date rk"]

all_stock['indicator'] = all_stock['mrv indicator'] + all_stock['senti indicator']

# nan indicator for non tradable stocks (we want to ignore these when we do our weighting algorithm)
# all_stock.loc[~all_stock['is_tradable'], 'indicator'] = np.nan

all_stock['indicator rk asc'] = all_stock.groupby('Date')['indicator'].rank(method="min", ascending=True) # bottom 5 stocks
all_stock['indicator rk desc'] = all_stock.groupby('Date')['indicator'].rank(method="max", ascending=False) # top 5 stocks


# filter to choose top and bottom stocks and add weighting algorithm
n_stocks = 5
winner = (all_stock['indicator rk desc'] <= n_stocks)
loser = (all_stock['indicator rk asc'] <= n_stocks)

all_stock.loc[winner, 'weight'] = 1
all_stock.loc[loser, 'weight'] = -1
all_stock[~(winner|loser), 'weight'] = 0

all_stock = all_stock[(all_stock['Date'] >= '2013-01-01')]

