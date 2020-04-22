import pandas as pd
import sys

# load series
ts = pd.read_csv(sys.argv[1])

# temperature series
temperature = pd.read_csv(sys.argv[2], decimal='.', sep=',')

ts['heat_target'] = ts['heat-storage'].diff() * 1e6
ts['heat_target'] = ts['heat_target'].apply(
        lambda x: x / 1.1905 if x < 0 else x / 0.84)
ts.loc[0, 'heat_target'] = 0

temperature_ff_max = temperature['Temperatur VL'].max()
temperature_ff_min = temperature['Temperatur VL'].min()
temperature_rf_max = temperature['Temperatur RL'].max()
temperature_rf_min = temperature['Temperatur RL'].min()

t_korr_ff_abs = 10
t_korr_rf_abs = 5
td_korr_rel = 2

ts['temperature_feed'] = (temperature['Temperatur VL'] - (
    temperature['Temperatur VL'] - temperature['Temperatur RL']) / td_korr_rel -
    t_korr_ff_abs).round(decimals=1)

ts['temperature_return'] = (temperature['Temperatur RL'] - (
    temperature['Temperatur RL'] - temperature_rf_min) / td_korr_rel -
    t_korr_rf_abs).round(decimals=1)

ts = ts.drop(columns=['heat-storage'])
ts = ts.rename(columns={'timeindex': 'time'})
ts.set_index('time')

ts.to_csv('input_timeseries.csv', index=False)
