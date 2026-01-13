import numpy as np

class TemperatureScaler:
    def __init__(self, T=1.0):
        self.T = T

    def calibrate(self, logits):
        return logits / self.T

    def softmax(self, z):
        e = np.exp(z - np.max(z))
        return e / e.sum()
