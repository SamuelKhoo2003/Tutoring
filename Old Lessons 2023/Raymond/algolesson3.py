

pos_dates = pm.list_data_dates('positions')
wgt_dates = pm.list_data_dates('weights')

last_pos_dates = pos_dates[-1]
last_wgt_dates = wgt_dates[-1]

print(f"...")
print(f"...")

old_pos = pm.read_positions(last_pos_dates)
old_stock_pos = old_pos[old_pos.index.str.contains('Equity')]
old_stock_values = (old_stock_pos['position'] * old_stock_pos['PX_LAST']).sum()
old_cash_values = old_pos.loc['hkd cur', 'position']
pos_dates = ["2024-5-7", "2023-6-7", ...] 
 
mylist = [2,3,4,5,4,6]
mylist.index(4)

