import argparse
import matplotlib.pyplot as plt
from .gbm.gbm_simulator import GBMSimulator


def simulate_gbm(y0, mu, sigma, T, N):
    """
    Simulate a Geometric Brownian Motion path.

    Parameters:
        y0 (float): Initial value Y(0).
        mu (float): Drift term.
        sigma (float): Volatility term.
        T (float): Total time for simulation.
        N (int): Number of time steps.

    Returns:
        tuple: t_values (np.ndarray), y_values (np.ndarray)
    """
    # Initialize simulator with user parameters
    simulator = GBMSimulator(y0, mu, sigma)
    t_values, y_values = simulator.simulate_path(T, N)
    return t_values, y_values


def plot_gbm(t_values, y_values, output=None):
    """
    Plot or save a Geometric Brownian Motion path.

    Parameters:
        t_values (np.ndarray): Array of time points.
        y_values (np.ndarray): Simulated GBM path values.
        output (str, optional): File path to save the plot as an image. If None, the plot will be displayed.
    """
    # Plot the path
    plt.plot(t_values, y_values, label="GBM Path")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.title("Geometric Brownian Motion Simulation")
    plt.legend()

    # Save or show plot
    if output:
        plt.savefig(output)
        print(f"Plot saved to {output}")
    else:
        plt.show()


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Simulate a Geometric Brownian Motion path."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Define the "simulate" command
    simulate_parser = subparsers.add_parser("simulate", help="Simulate a GBM path")
    simulate_parser.add_argument(
        "--y0", type=float, required=True, help="Initial value Y(0)"
    )
    simulate_parser.add_argument("--mu", type=float, required=True, help="Drift term")
    simulate_parser.add_argument(
        "--sigma", type=float, required=True, help="Volatility term"
    )
    simulate_parser.add_argument(
        "--T", type=float, required=True, help="Total time for simulation"
    )
    simulate_parser.add_argument(
        "--N", type=int, required=True, help="Number of time steps"
    )
    simulate_parser.add_argument(
        "--output", type=str, help="File path to save the plot as an image"
    )

    # Parse arguments
    args = parser.parse_args()

    # Check which command is called
    if args.command == "simulate":
        # Call the simulate function
        t_values, y_values = simulate_gbm(args.y0, args.mu, args.sigma, args.T, args.N)

        # Call the plot function
        plot_gbm(t_values, y_values, args.output)


if __name__ == "__main__":
    main()
