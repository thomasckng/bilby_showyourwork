import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from bilby.gw.result import CBCResult
from kde_contour import Bounded_1d_kde, kdeplot_2d_clevels
import paths

sns.set_theme(palette='colorblind', font_scale=1.5)

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

nsamples = 5000
rng = np.random.default_rng(1234)

result = pd.read_feather(paths.data/"samples_posterior_birefringence.feather")
result = result[result.event == "GW200129_065458"]
result = result.sample(n=nsamples, random_state=rng)
result['with'] = np.full(len(result), "HLV")
result['cos_iota'] = np.cos(result['iota'])

result_without_H1 = CBCResult.from_json(filename=paths.data/"GW200129_065458_birefringence_without_H1.json.gz").posterior
result_without_H1 = result_without_H1.sample(n=nsamples, random_state=rng)
result_without_H1['with'] = np.full(len(result_without_H1), "LV")
result_without_H1['cos_iota'] = np.cos([float(result_without_H1['iota'][i]) for i in result_without_H1.index])

result_without_L1 = CBCResult.from_json(filename=paths.data/"GW200129_065458_birefringence_without_L1.json.gz").posterior
result_without_L1 = result_without_L1.sample(n=nsamples, random_state=rng)
result_without_L1['with'] = np.full(len(result_without_L1), "HV")
result_without_L1['cos_iota'] = np.cos([float(result_without_L1['iota'][i]) for i in result_without_L1.index])

result_without_V1 = CBCResult.from_json(filename=paths.data/"GW200129_065458_birefringence_without_V1.json.gz").posterior
result_without_V1 = result_without_V1.sample(n=nsamples, random_state=rng)
result_without_V1['with'] = np.full(len(result_without_V1), "HL")
result_without_V1['cos_iota'] = np.cos([float(result_without_V1['iota'][i]) for i in result_without_V1.index])

result_all = pd.concat([result,result_without_H1,result_without_L1,result_without_V1], ignore_index=True)

def kdeplot2d(x, y, mask=None, **kws):
    kws.pop('label', None)
    kdeplot_2d_clevels(xs=x[mask], ys=y[mask], auto_bound=True, **kws)

def kdeplot1d(x, mask=None, **kws):
    x = x[mask]
    if np.all(x.isna()):
        return
    df = pd.DataFrame({'x': x, 'y': Bounded_1d_kde(x, xlow=min(x), xhigh=max(x))(x)})
    df = df.sort_values(['x'])
    if kws.pop('fill', False):
        plt.fill_between(df['x'], df['y'], np.zeros(len(x)), alpha=0.2, **kws)
    plt.plot(df['x'], df['y'], **kws)

p = list(sns.color_palette())[:3] + ['0.35']
vars = ['kappa', 'luminosity_distance', 'cos_iota']
g = sns.PairGrid(data=result_all,
                 vars=vars,
                 corner=True, hue='with', diag_sharey=False,
                 layout_pad=0., palette=p
                )

m = result_all['with'] == "HLV"
g.map_lower(kdeplot2d, mask=m, levels=[0.90], fill=True, alpha=0.2, colors=[p[0]])
g.map_lower(kdeplot2d, mask=m, levels=[0.90])
g.map_diag(kdeplot1d, mask=m, fill=True)

m = (result_all['with'] == "HV") | (result_all['with'] == "LV")
g.map_lower(kdeplot2d, mask=m, linewidths=2, levels=[0.90])
g.map_diag(kdeplot1d, mask=m, linewidth=2, fill=False)

m = result_all['with'] == "HL"
g.map_lower(kdeplot2d, mask=m, linewidths=2, linestyles='--', levels=[0.90], zorder=100)
g.map_diag(kdeplot1d, mask=m, linewidth=2, linestyle='--', fill=False, zorder=100)

# g.axes[0,0].set_xlim(-1., 1.)
# g.axes[0,0].set_ylim(0)
# g.axes[1,1].set_xlim(0, 2000)
# g.axes[1,1].set_ylim(0)
# g.axes[2,2].set_xlim(-1., 1.)
# g.axes[2,2].set_ylim(0)

# g.axes[1,0].set_xlim(-1., 1.)
# g.axes[1,0].set_ylim(0, 2000)
# g.axes[2,0].set_xlim(-1., 1.)
# g.axes[2,0].set_ylim(-1., 1.)
# g.axes[2,1].set_xlim(0, 2000)
# g.axes[2,1].set_ylim(-1., 1.)

# for i in range(len(vars)):
#     g.axes[i,i].set_xlim(result[vars[i]].min(), result[vars[i]].max())
#     g.axes[i,i].set_ylim(0)
#     for j in range(i):
#         g.axes[i,j].set_xlim(result[vars[j]].min(), result[vars[j]].max())
#         g.axes[i,j].set_ylim(result[vars[i]].min(), result[vars[i]].max())

g.axes[2,0].set_xlabel(r"$\kappa$")
g.axes[1,0].set_ylabel(r"$d_L$ (Mpc)")
g.axes[2,1].set_xlabel(r"$d_L$ (Mpc)")
g.axes[2,0].set_ylabel(r"$\cos\iota$")
g.axes[2,2].set_xlabel(r"$\cos\iota$")

plt.subplots_adjust(wspace=0.05, hspace=0.05)

for k, c in zip(["HLV", "HV", "LV", "HL"], p):
    g.axes[0,0].plot([], c=c, lw=2, ls='--' if k=="HL" else '-', label=k)
g.axes[0,0].legend(loc='center left', bbox_to_anchor=(1.1, 0.5), frameon=False)

g.savefig(fname=paths.figures/"corner_GW200129.pdf", bbox_inches="tight", dpi=300)
