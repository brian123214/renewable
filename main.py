import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
class Radar(object):
    def __init__(self, figure, title, labels, rect=None):
        if rect is None:
            rect = [0.05, 0.05, 0.9, 0.9]

        self.n = len(title)
        self.angles = np.arange(0, 360, 360.0/self.n)

        self.axes = [figure.add_axes(rect, projection='polar', label='axes%d' % i) for i in range(self.n)]

        self.ax = self.axes[0]
        self.ax.set_thetagrids(self.angles, labels=title, fontsize=12)

        for ax in self.axes[1:]:
            ax.patch.set_visible(False)
            ax.grid(False)
            ax.xaxis.set_visible(False)

        for ax, angle, label in zip(self.axes, self.angles, labels):
            ax.set_rgrids(range(1, 6), angle=angle, labels=label)
            ax.spines['polar'].set_visible(False)
            ax.set_ylim(0, 5)

    def plot(self, values, *args, **kw):
        angle = np.deg2rad(np.r_[self.angles, self.angles[0]])
        values = np.r_[values, values[0]]
        self.ax.plot(angle, values, *args, **kw)


if __name__ == '__main__':
    fig = plt.figure(figsize=(8, 8))

    # tit = list('ABCDEFGHIJKJ')  # 12x
    # tit = ["Nuclear", "Geothermal", "Hydropower", "Hydrogen Fuel Cell", "Solar Power"]
    tit = ["Land Usage sq km/twh per year", "Median electricity cost USD/mwh", "Liters of water/kwh", "CO2 Produced g/kwh"]

    lab = [
        [14, 28, 42, 56, 70],
        [20, 40, 60, 80, 100],
        [1.5, 3, 4.5, 6, 7.5], # 12, 
        [18, 36, 54, 72, 90]
    ]

    radar = Radar(fig, tit, lab)
    radar.plot([2.4/14, 32.0/20, 1.3, 12.0/18],  '-', lw=2, color='b', alpha=0.4, label='Nuclear')
    radar.plot([7.5/14, 99.0/20, 1.2, 5], '-', lw=2, color='r', alpha=0.4, label='Geothermal')
    radar.plot([54/14, 68.0/20, 5, 18.5/18], '-', lw=2, color='g', alpha=0.4, label='Hydropower')
    radar.plot([5, 39.0/20, 0, 11.0/18], '-', lw=2, color='m', alpha=0.4, label='Wind Power')

    radar.ax.legend()
pl.show()

# unfortunately... we forgot to keep track of sources
