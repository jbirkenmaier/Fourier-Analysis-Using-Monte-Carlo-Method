import random

import matplotlib.pyplot as plt
import math
import numpy as np
import random


def function(position):
    return 3 * math.sin(position) + 5


class Sound:
    def __init__(self, definition_space):
        self.definition_space = definition_space

    def plot_self(self):
        plt.plot(self.definition_space, [function(i) for i in self.definition_space], color='r')


class Fourier:
    def __init__(self, foreign_sound, num_of_harmonics):
        self.definition_space = foreign_sound.definition_space
        self.foreign_sound = [function(i) for i in foreign_sound.definition_space]
        self.num_of_harmonics = num_of_harmonics
        self.harmonics_coefficients = [1 for i in range(num_of_harmonics)]
        self.harmonics_phases = [1 for i in range(num_of_harmonics)]
        self.harmonics_offset = [5 for i in range(num_of_harmonics)]
        self.cos_harmonics_coefficients = [1 for i in range(num_of_harmonics)]
        self.cos_harmonics_phases = [1 for i in range(num_of_harmonics)]
        self.cos_harmonics_offset = [5 for i in range(num_of_harmonics)]
        self.total_fourier_approx()
        self.total_loss = 0
        self.calculate_total_loss()

    def fourier_approximation(self, pos):
        approx = 0
        for i in range(self.num_of_harmonics):
            approx += self.harmonics_coefficients[i]/self.num_of_harmonics * math.sin(self.foreign_sound[pos] * 2 * math.pi / (i + 1)+self.harmonics_phases[i]) + \
                      self.harmonics_offset[i]
        return approx

    def loss(self, pos):
        return np.abs(self.fourier_approximation(pos) - self.foreign_sound[pos])

    def fourier_analysis(self):
        self.total_loss = 0
        for element in range(len(self.foreign_sound)):
            #print(self.total_loss)
            self.total_loss += self.loss(element)

    def plot_self(self, x):
        plt.plot(x, self.total_fourier_approx(), label=self.total_loss)

    #we have phases and coefficients that whe can manipulate to minimize the loss function.
    #our premise is that we have no idea what the function of the sound wave that we are trying to approximate is
    #for that we change parameters step by step. If they minimize the loss, we apply the change. If not, we discard it
    def minimize_loss(self):
        flow = math.pi/2
        while self.total_loss > 50:
            current_loss = self.total_loss
            start_harmonics_coefficient = [i for i in range(self.num_of_harmonics)]
            for i in range(self.num_of_harmonics):
                start_harmonics_coefficient[i] = self.harmonics_coefficients[i]
                self.harmonics_coefficients[i] += random.uniform(-flow, flow)
            self.fourier_analysis()
            if np.abs(current_loss) > np.abs(self.total_loss):
                #self.plot_self(self.definition_space)
                continue
            elif np.abs(current_loss) < np.abs(self.total_loss):
                for i in range(self.num_of_harmonics):
                    self.harmonics_coefficients[i] = start_harmonics_coefficient[i]
                    self.fourier_analysis()
            elif np.abs(current_loss) == np.abs(self.total_loss):
                continue
            print(self.total_loss)

            current_loss = self.total_loss
            start_harmonics_phases = [i for i in range(self.num_of_harmonics)]
            for i in range(self.num_of_harmonics):
                start_harmonics_phases[i] = self.harmonics_phases[i]
                self.harmonics_phases[i] += random.uniform(-flow, flow)
            self.fourier_analysis()
            if np.abs(current_loss) > np.abs(self.total_loss):
                #self.plot_self(self.definition_space)
                continue
            elif np.abs(current_loss) < np.abs(self.total_loss):
                for i in range(self.num_of_harmonics):
                    self.harmonics_phases[i] = start_harmonics_phases[i]
                    self.fourier_analysis()
            elif np.abs(current_loss) == np.abs(self.total_loss):
                continue

            current_loss = self.total_loss
            start_harmonics_phases = [i for i in range(self.num_of_harmonics)]
            for i in range(self.num_of_harmonics):
                start_harmonics_phases[i] = self.harmonics_phases[i]
                self.harmonics_phases[i] += random.uniform(-flow, flow)
            self.fourier_analysis()
            if np.abs(current_loss) > np.abs(self.total_loss):
                #self.plot_self(self.definition_space)
                continue
            elif np.abs(current_loss) < np.abs(self.total_loss):
                for i in range(self.num_of_harmonics):
                    self.harmonics_phases[i] = start_harmonics_phases[i]
                    self.fourier_analysis()
            elif np.abs(current_loss) == np.abs(self.total_loss):
                continue

            current_loss = self.total_loss
            start_harmonics_offsets = [i for i in range(self.num_of_harmonics)]
            for i in range(self.num_of_harmonics):
                start_harmonics_offsets[i] = self.harmonics_offset[i]
                self.harmonics_offset[i] += random.uniform(-flow, flow)
            self.fourier_analysis()
            if np.abs(current_loss) > np.abs(self.total_loss):
                #self.plot_self(self.definition_space)
                continue
            elif np.abs(current_loss) < np.abs(self.total_loss):
                for i in range(self.num_of_harmonics):
                    self.harmonics_offset[i] = start_harmonics_offsets[i]
                    self.fourier_analysis()
            elif np.abs(current_loss) == np.abs(self.total_loss):
                continue

    def calculate_total_loss(self):
        for i in range(len(self.total_fourier_approx())):
            self.total_loss += np.abs(self.total_fourier_approx()[i] - self.foreign_sound[i])

    def total_fourier_approx(self):
        return [self.fourier_approximation(i) for i in range(len(self.foreign_sound))]
