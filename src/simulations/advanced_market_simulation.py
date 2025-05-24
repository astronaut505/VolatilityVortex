# Advanced Market Simulation Engine
# This script implements advanced market simulation models, including Ornstein-Uhlenbeck, Jump Diffusion, Heston, ABM, and GBM models.

import numpy as np

class MarketSimulation:
    @staticmethod
    def ornstein_uhlenbeck_process(theta, mu, sigma, X0, T, dt):
        """
        Simulates the Ornstein-Uhlenbeck process.
        """
        n = int(T / dt)
        X = np.zeros(n)
        X[0] = X0
        for t in range(1, n):
            dW = np.random.normal(0, np.sqrt(dt))
            X[t] = X[t-1] + theta * (mu - X[t-1]) * dt + sigma * dW
        return X

    @staticmethod
    def jump_diffusion_model(mu, sigma, lambda_, jump_mean, jump_std, X0, T, dt):
        """
        Simulates the Jump Diffusion model.
        """
        n = int(T / dt)
        X = np.zeros(n)
        X[0] = X0
        for t in range(1, n):
            dW = np.random.normal(0, np.sqrt(dt))
            dN = np.random.poisson(lambda_ * dt)
            J = np.random.normal(jump_mean, jump_std) if dN > 0 else 0
            X[t] = X[t-1] + mu * dt + sigma * dW + J
        return X

    @staticmethod
    def heston_model(mu, kappa, theta, xi, V0, X0, T, dt):
        """
        Simulates the Heston model.
        """
        n = int(T / dt)
        X = np.zeros(n)
        V = np.zeros(n)
        X[0] = X0
        V[0] = V0
        for t in range(1, n):
            dW = np.random.normal(0, np.sqrt(dt))
            dZ = np.random.normal(0, np.sqrt(dt))
            V[t] = max(V[t-1] + kappa * (theta - V[t-1]) * dt + xi * np.sqrt(max(V[t-1], 0)) * dZ, 1e-6)  # Ensure variance is non-zero
            X[t] = X[t-1] + mu * X[t-1] * dt + np.sqrt(V[t]) * X[t-1] * dW
        return X, V

    @staticmethod
    def arithmetic_brownian_motion(mu, sigma, X0, T, dt):
        """
        Simulates Arithmetic Brownian Motion (ABM).

        :param mu: Drift.
        :param sigma: Volatility.
        :param X0: Initial price.
        :param T: Total time.
        :param dt: Time step.
        :return: Simulated price path.
        """
        n = int(T / dt)
        X = np.zeros(n)
        X[0] = X0
        for t in range(1, n):
            dW = np.random.normal(0, np.sqrt(dt))
            X[t] = X[t-1] + mu * dt + sigma * dW
        return X

    @staticmethod
    def geometric_brownian_motion(mu, sigma, X0, T, dt):
        """
        Simulates Geometric Brownian Motion (GBM).

        :param mu: Drift.
        :param sigma: Volatility.
        :param X0: Initial price.
        :param T: Total time.
        :param dt: Time step.
        :return: Simulated price path.
        """
        n = int(T / dt)
        X = np.zeros(n)
        X[0] = X0
        for t in range(1, n):
            dW = np.random.normal(0, np.sqrt(dt))
            X[t] = X[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * dW)
        return X

    @staticmethod
    def monte_carlo_simulation(simulation_func, params, num_simulations):
        """
        Runs Monte Carlo simulations for a given market simulation function.

        :param simulation_func: The market simulation function to use (e.g., ABM, GBM).
        :param params: Parameters for the simulation function.
        :param num_simulations: Number of Monte Carlo simulations to run.
        :return: List of simulation results.
        """
        results = []
        for _ in range(num_simulations):
            result = simulation_func(**params)
            results.append(result)
        return results

# Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    # Ornstein-Uhlenbeck Example
    ou_process = MarketSimulation.ornstein_uhlenbeck_process(theta=0.7, mu=100, sigma=2, X0=95, T=1.0, dt=0.01)
    print("Ornstein-Uhlenbeck Process Simulated.")

    # Jump Diffusion Example
    jump_diffusion = MarketSimulation.jump_diffusion_model(mu=0.1, sigma=1.5, lambda_=0.5, jump_mean=5, jump_std=2, X0=100, T=1.0, dt=0.01)
    print("Jump Diffusion Model Simulated.")

    # Heston Model Example
    heston_prices, heston_vols = MarketSimulation.heston_model(mu=0.05, kappa=2.0, theta=0.04, xi=0.1, V0=0.04, X0=100, T=1.0, dt=0.01)
    print("Heston Model Simulated.")

    # ABM Example
    abm_process = MarketSimulation.arithmetic_brownian_motion(mu=0.1, sigma=1.0, X0=100, T=1.0, dt=0.01)
    print("Arithmetic Brownian Motion Simulated.")

    # GBM Example
    gbm_process = MarketSimulation.geometric_brownian_motion(mu=0.1, sigma=0.2, X0=100, T=1.0, dt=0.01)
    print("Geometric Brownian Motion Simulated.")

    # Monte Carlo Simulation Example
    mc_results = MarketSimulation.monte_carlo_simulation(MarketSimulation.geometric_brownian_motion, {'mu': 0.1, 'sigma': 0.2, 'X0': 100, 'T': 1.0, 'dt': 0.01}, num_simulations=10)
    print("Monte Carlo Simulations Completed.")
