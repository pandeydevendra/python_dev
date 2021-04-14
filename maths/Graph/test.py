import pylab as pl
import numpy as np

# Sample data
X = np.linspace(-5, 105, 2000, endpoint = True)
Cosine, Sine = 0.45 * np.cos(0.2*X) + 0.5, 0.45 * np.sin(0.2*X) + 0.5


# Plot
pl.plot(X, Cosine)
pl.plot(X, Sine)


# Set x and y limits
pl.xlim(0.0, 100.0)
pl.ylim(0.0,   1.0)


# Set ticks for x and y axis
pl.xticks(np.linspace(0.0, 100.0, 11, endpoint = True))
pl.yticks(np.linspace(0.0,   1.0, 11, endpoint = True))


pl.show()