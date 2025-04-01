# Example of declaring a dataframe (using Numpy date_range function):
# In [5]: dates = pd.date_range("20130101", periods=6)

# In [6]: dates
# Out[6]: 
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')

In [7]: df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

In [8]: df
Out[8]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988

# def last_open_prc_available(df)
#    filt = ~"PXlast".isna() & ~"PxOpen".isna()
#     return filt

def ss_pct(df, w):
    ss_rk = df['SHORT_SELL_NUM_SHARES']/df['VOLUME']
    rolling_ss_rk = ss_rk.rolling(20).mean()
    final_ss_rk = -rolling_ss_rk.ewm(w).mean()
    return final_ss_rk

mynum = 5