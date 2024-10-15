---
layout: default
title: "Constraining gravitational wave amplitude birefringence with GWTC-3"
---

<script type="text/javascript" async
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

**Thomas C. K. Ng** (The Chinese University of Hong Kong),
**Maximiliano Isi** (Flatiron Institute),
**Kaze W. K. Wong** (Flatiron Institute),
**Will M. Farr** (Flatiron Institute & Stony Brook University)

## Abstract

1. **Objective**: exploring the possibility of **amplitude birefringence** in gravitational waves (GW)
2. **Method**: performing **parameter estimation** (PE) on 71 events from GWTC-2.1 and 3
3. **Result**: The most precise constraint on amplitude birefringence to date with an **order-of-magnitude improvement** over previous studies

## Paper Summary

**GW Amplitude Birefringence**:
- **Predicted effect** in parity-odd theories like **Chern-Simons gravity** (general relativity (GR) predicts there isn't)
- Effect: one polarization is **enhanced**, another is **suppressed** during **propagation**

**Illustration**:

<img src="{{site.url}}{{site.baseurl}}/public/image/birefringence.pdf"/>

the **upper panel** of the figure above shows the absolute **amplitude** of the left and right **polarization** in the **frequency domain**. The dotted lines show the original waveforms with GR. With the effect of birefringence, one polarization is enhanced while the other is suppressed, with **higher frequency** components of the waveforms being **modified more**. The **lower panel** shows the same effect in the **time domain**.

The **observed waveform** a comoving distance $$d_C$$ away from the source can be written as

$$h_{L/R}^{\mathrm{BR}}(f) = h_{L/R}^{\mathrm{GR}}(f) \times \exp\left(\pm\kappa\, d_C \frac{f}{100\,\mathrm{Hz}}\right)\,,$$

where the emitted waveform $$h_{L/R}^{\mathrm{GR}}$$ is modified by an exponential birefringent factor to yield the observed waveform $$h_{L/R}^{\mathrm{BR}}$$.
The overall magnitude of this effect for a given frequency $$f$$ is set by an **attenuation coefficient**, **$$\kappa$$**, which encodes the **intrinsic strength** of the birefringence.
Note that $$\kappa=0$$ represents no amplitude birefringence, and the observed waveform is the same as the one predicted by GR.

## Method

**Aim**: constrain the strength of GW amplitude birefringence, which is quantified by $$\kappa$$

- Modify **Bilby** to include the effect of amplitude birefringence
- Perform **PE** on 71 BBHs with false alarm rate < 1/yr
- Two sets of collective analyses:
    1. **Restricted**: assume birefringence is a property of spacetime
    - give a **global common value** of $$\kappa$$ for all events
    2. **Generic**: assume $$\kappa$$ inferred from each event is a **random variable** drawn from a **Gaussian** distribution
    - investigate possible diagnostics and explore extra physics

## Result

<img src="{{site.url}}{{site.baseurl}}/public/image/violin_kappa.pdf"/>

- Individual posteriors colored by magnitude of deviation $$\mu/\sigma$$
- **Restricted result** (blue region):
    - **$$\kappa=-0.019^{+0.038}_{-0.029} \, \mathrm{Gpc^{-1}}$$** (90% credible interval)

### Hierarchical analysis (Generic Result)

<img src="{{site.url}}{{site.baseurl}}/public/image/corner_Gaussian.pdf"/>

- Lack of birefringence is supported within 90% credibility
- $$\sigma$$ posterior peaks visibly **away from the origin**
    - Indicating some preference for a nonzero variance
- Further observations are needed to determine whether there is true evidence for a nonvanishing variance in this population
- **GW200129** is a **potentially-contaminated event**

## Notable Events

### GW170818

<img src="{{site.url}}{{site.baseurl}}/public/image/corner_GW170818.pdf"/>

- **Most displaced** posterior from $$\kappa=0$$
- GR analysis gives $$\cos\iota=-1$$ ($$\iota$$: inclination angle)
    - Observed signal can be considered to be **purely left-handed**
- With birefringence, the same signal can be **reconstructed with different $$\iota$$**, as long as $$d_L$$ can also be enhanced to give the right amount of birefringence and overall signal power

- Difficult to determine why the GW170818 data gives this posterior structure
    - May be **related** to the **support** it has for **precession**
    - Birefringence **reduces** the **support** for **precession** (see top-right panel)
- If only a short portion of the signal is observed, adjusting $$\chi_p$$ and $$\kappa$$ may yield similar results as long as $$d_L$$ and $$\iota$$ can be tuned accordingly
    - With prior that favors larger distances, we get higher probability density with $$\kappa\neq0$$.


### GW190521

<img src="{{site.url}}{{site.baseurl}}/public/image/corner_GW190521.pdf"/>

- **Bimodal** posterior distribution on $$\kappa$$
- **Least support** for $$\kappa=0$$

- Two peaks of the $$\kappa$$ distribution correspond to two solutions that arise from respective modes in the inclination
- Without certainty about the ratio between two polarization
    - Not possible to distinguish between +ve / -ve $$\kappa$$
- Birefringence **changes** the posterior on **$$\chi_\mathrm{eff}$$**
- Situation for **GW190521** is **similar** to that of **GW170818**
    - Degeneracies are likely increased by the **heavier mass** of the system, which **reduces** the observed **number of cycles**


### $$\kappa$$ correlated with $$q$$ & spins

<img src="{{site.url}}{{site.baseurl}}/public/image/mass_ratio.pdf"/>

- Examine the effect of birefringence on other parameters with two events as examples
    - Both events give **bimodal** $$\kappa$$ posteriors, but do not rule out $$\kappa=0$$
- GW170104
    - **increase** the preference for **asymmetric masses**
    - **decrease** the inferred level of **precession**
- GW191105
    - **increase** the preference for **symmetric masses**
- Coupling between $$q$$ and $$\kappa$$ is likely limited by the fact that **changes in $$q$$** alone **cannot** produce significant **amplitude modulations**

### GW200129

<img src="{{site.url}}{{site.baseurl}}/public/image/corner_GW200129.pdf"/>

- Second-largest deviation from $$\kappa=0$$
- May have been affected by a **glitch** in the Virgo instrument

- Additional **PE** runs were performed with only **two detectors at a time**
    - Results suggest that the Virgo data is **responsible** for $$\kappa<0$$
- **Excluding** it from the collective analyses did **not** significantly impact the results
- Further work is needed to understand the effect of the glitch

## Conclusion

- Provided a significant **improvement** in the **constraint** on frequency-dependent **amplitude birefringence** compared to previous studies

- Identified **new correlations** between **attenuation** and **binary parameters**
    - particularly the relevance of **spins** and their partial degeneracy with $$\kappa$$, as well as expected correlations with $$\iota$$ and $$d_L$$
- more events are needed to understand the spread in the $$\kappa$$ distribution obtained from the hierarchical analysis

## More about the author

<img src="{{site.url}}{{site.baseurl}}/public/image/thomas.jpeg"/>

Thomas Ng is a M.Phil. student at The Chinese University of Hong Kong.
More about Thomas: [Thomas's Personal Website](https://thomasckng.github.io)
