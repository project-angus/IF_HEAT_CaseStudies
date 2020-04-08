import pandas as pd
from matplotlib import pyplot as plt
import sys
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# load series
ts = pd.read_csv(sys.argv[1], index_col=0)

ts.index = pd.to_datetime(ts.index)

ts['charging'] = ts['Q_target'] > 0
ts['discharging'] = ts['Q_target'] < 0
charging = ts.where(ts['charging'])
discharging = ts.where(ts['discharging'])

num_ticks = 6

fig, ax = plt.subplots(2, 1)
ax[0].scatter(charging.index, charging['Q_actual'] / charging['Q_target'], c=charging['Q_actual'] / charging['Q_target'])
ax[0].set_ylabel('actual to target heat transfer')
ax[0].set_xlabel('time')
ax[0].set_title('charging')
ax[0].grid()
ax[0].set_xlim(charging.index[0], charging.index.dropna()[-1])
ax[0].locator_params(axis='x', nbins=num_ticks + 1)

ax[1].scatter(discharging.index, -discharging['Q_actual'] / discharging['Q_target'], c=-discharging['Q_actual'] / discharging['Q_target'])
ax[1].set_ylabel('actual to target heat transfer')
ax[1].set_xlabel('time')
ax[1].set_title('discharging')
ax[1].grid()
ax[1].set_xlim(discharging.index[0], discharging.index.dropna()[-1])
ax[1].locator_params(axis='x', nbins=num_ticks + 1)

plt.tight_layout()

fig.savefig('heat_transfer.pdf')

fig, ax = plt.subplots(2, 1)
ax[0].scatter(charging.index, charging['T_rf_sto'], Color='r')
ax[0].scatter(charging.index, charging['T_ff_sto'], Color='b')
ax[0].set_ylabel('temperature')
ax[0].set_xlabel('time')
ax[0].set_title('charging temperature curves')
ax[0].grid()
ax[0].set_xlim(charging.index[0], charging.index.dropna()[-1])
ax[0].locator_params(axis='x', nbins=num_ticks + 1)

ax[1].scatter(discharging.index, discharging['T_rf_sto'], Color='r')
ax[1].scatter(discharging.index, discharging['T_ff_sto'], Color='b')
ax[1].set_ylabel('temperature')
ax[1].set_xlabel('time')
ax[1].set_title('discharging temperature curves')
ax[1].grid()
ax[1].set_xlim(discharging.index[0], discharging.index.dropna()[-1])
ax[1].locator_params(axis='x', nbins=num_ticks + 1)

plt.tight_layout()

fig.savefig('temperature_curves.pdf')

fig, ax = plt.subplots(3, 1)

ax[0].scatter(ts.index, ts['pp_err'] * 1, c=ts['pp_err'])
ax[0].set_ylabel('error in simulation')
ax[0].set_xlabel('time')
ax[0].set_title('errors')
ax[0].set_yticks([0, 1])
ax[0].set_yticklabels(['no error', 'error'])
ax[0].grid()
ax[0].set_xlim(ts.index[0], ts.index.dropna()[-1])
ax[0].locator_params(axis='x', nbins=num_ticks + 1)

ax[1].scatter(charging.index, charging['T_ff_sys'] - charging['T_rf_sto'], c=ts['pp_err'])
ax[1].set_ylabel('T_ff_sys - T_rf_sto')
ax[1].set_xlabel('time')
ax[1].set_title('errors')
ax[1].grid()
ax[1].set_xlim(charging.index[0], charging.index.dropna()[-1])
ax[1].locator_params(axis='x', nbins=num_ticks + 1)

ax[2].scatter(discharging.index, discharging['T_rf_sto'] - discharging['T_ff_sto'], c=ts['pp_err'])
ax[2].set_ylabel('T_ff_sto - T_rf_sto')
ax[2].set_xlabel('time')
ax[2].set_title('errors')
ax[2].grid()
ax[2].set_xlim(discharging.index[0], discharging.index.dropna()[-1])
ax[2].locator_params(axis='x', nbins=num_ticks + 1)

plt.tight_layout()

fig.savefig('errors.pdf')
