# Main Script for Running Simulations
# This script integrates all components, runs simulations, and generates CSV outputs.

import csv
import numpy as np
from simulations.advanced_market_simulation import MarketSimulation
from strategies.enhanced_pricing_strategy import PricingStrategy
from executions.advanced_order_execution import OrderExecution
from core.risk_management import RiskManagement

def run_simulation():
    """
    Runs the complete simulation and generates results.
    """
    # Parameters
    T = 1.0
    dt = 0.01
    time_steps = int(T / dt)
    time = np.linspace(0, T, time_steps)

    # Market Simulation
    ou_process = MarketSimulation.ornstein_uhlenbeck_process(theta=0.7, mu=100, sigma=2, X0=95, T=T, dt=dt)
    jump_diffusion = MarketSimulation.jump_diffusion_model(mu=0.1, sigma=1.5, lambda_=0.5, jump_mean=5, jump_std=2, X0=100, T=T, dt=dt)
    heston_prices, heston_vols = MarketSimulation.heston_model(mu=0.05, kappa=2.0, theta=0.04, xi=0.1, V0=0.04, X0=100, T=T, dt=dt)

    # Pricing Strategy (Dummy Example)
    features = np.array([1.0, 2.0, 3.0])
    class DummyModel:
        def predict(self, features):
            return [0.01, 0.02]  # Dummy bid and ask spreads
    model = DummyModel()
    bid, ask = PricingStrategy.machine_learning_based_strategy(features, model)

    # Order Execution (Dummy Example)
    adjusted_size = OrderExecution.adaptive_execution(order_size=100, market_volatility=0.2, risk_tolerance=0.5)

    # Risk Management (Dummy Example)
    returns = np.random.normal(0.02, 0.01, time_steps)
    metrics = RiskManagement.risk_adjusted_metrics(returns, risk_free_rate=0.01)

    # Generate CSV Output
    with open("simulation_results.csv", "w", newline="") as csvfile:
        fieldnames = ["Time", "OU_Process", "Jump_Diffusion", "Heston_Prices", "Heston_Vols", "Bid", "Ask", "Adjusted_Size", "Sharpe_Ratio", "Sortino_Ratio"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for t in range(time_steps):
            writer.writerow({
                "Time": time[t],
                "OU_Process": ou_process[t],
                "Jump_Diffusion": jump_diffusion[t],
                "Heston_Prices": heston_prices[t],
                "Heston_Vols": heston_vols[t],
                "Bid": bid,
                "Ask": ask,
                "Adjusted_Size": adjusted_size,
                "Sharpe_Ratio": metrics["Sharpe Ratio"],
                "Sortino_Ratio": metrics["Sortino Ratio"]
            })

    print("Simulation completed. Results saved to simulation_results.csv.")

if __name__ == "__main__":
    run_simulation()
