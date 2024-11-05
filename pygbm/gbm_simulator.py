import numpy as np
from .base_simulator import BaseSimulator

class GBMSimulator(BaseSimulator):
    def __init__(self, y0, mu, sigma):
        """
        Initializes the GBM Simulator with initial value, drift, and volatility.
        
        Parameters:
            y0 (float): Initial value Y(0).
            mu (float): Drift term.
            sigma (float): Volatility term.
        """
        super().__init__(y0)
        self.mu = mu
        self.sigma = sigma

    def simulate_path(self, T, N):
        """
        Simulates a path of the Geometric Brownian Motion.
        
        Parameters:
            T (float): Total time for simulation.
            N (int): Number of time steps.

        Returns:
            t_values (np.ndarray): Array of time points.
            y_values (np.ndarray): Simulated GBM path values.
        """
        dt = T / N
        t_values = np.linspace(0, T, N+1)
        y_values = np.zeros(N+1)
        y_values[0] = self.y0
        
        for i in range(1, N+1):
            # Brownian motion increment
            dB = np.random.normal(0, np.sqrt(dt))
            # GBM increment based on the given formula
            y_values[i] = y_values[i-1] * np.exp((self.mu - 0.5 * self.sigma**2) * dt + self.sigma * dB)
        
        return t_values, y_values
