import function_library as fl
import numpy as np
import math
import matplotlib.pyplot as plt


def sound_wave(x):
    return np.sin(x)


x = np.linspace(-4 * math.pi, 4 * math.pi, 1000)
sound = fl.Sound(x)
sound.plot_self()

fourier = fl.Fourier(sound,50)
fourier.fourier_analysis()
fourier.minimize_loss()
print(fourier.harmonics_coefficients)
print(fourier.harmonics_phases)
print(fourier.harmonics_offset)
fourier.plot_self(x)
#plt.legend()
plt.show()