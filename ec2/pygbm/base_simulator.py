class BaseSimulator:
    def __init__(self, y0):
        """
        Initializes the simulator with an initial value.
        
        Parameters:
            y0 (float): Initial value Y(0).
        """
        self.y0 = y0

    def simulate_path(self, T, N):
        """
        Simulates a path over time. To be implemented in derived classes.
        
        Parameters:
            T (float): Total time for simulation.
            N (int): Number of time steps.

        Returns:
            t_values (np.ndarray): Array of time points.
            y_values (np.ndarray): Simulated path values.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
