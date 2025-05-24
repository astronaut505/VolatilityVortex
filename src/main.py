# Enhanced Main Script for Running Simulations
# This script integrates all components, runs simulations, and generates comprehensive outputs.

import csv
import numpy as np
import pandas as pd
import sys
import os
from simulations.advanced_market_simulation import MarketSimulation
from strategies.enhanced_pricing_strategy import PricingStrategy
from executions.advanced_order_execution import OrderExecution
from core.risk_management import RiskManagement
from utils.data_analysis import DataAnalysis
from utils.extensibility import Extensibility

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

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

    # Integrate ABM/GBM and Poisson-based trade arrivals
    abm_prices = MarketSimulation.arithmetic_brownian_motion(mu=0.1, sigma=1.0, X0=100, T=T, dt=dt)
    gbm_prices = MarketSimulation.geometric_brownian_motion(mu=0.1, sigma=1.0, X0=100, T=T, dt=dt)

    trade_arrivals = OrderExecution.simulate_trade_arrivals(lambda_rate=0.5, T=T, dt=dt)

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

    # Extensibility (Dummy Examples)
    combined_output = Extensibility.hybrid_model(traditional_model_output=0.05, ml_model_output=0.08, weight=0.6)
    impact_score = Extensibility.behavioral_analysis(trader_actions=[1, -1, 1, 1, -1], market_conditions=[0.5, -0.2, 0.3, 0.4, -0.1])
    avg_spread, avg_depth = Extensibility.microstructure_analysis(order_book_data=[
        {"bid": 100, "ask": 101, "depth": 500},
        {"bid": 99.5, "ask": 100.5, "depth": 450},
        {"bid": 100.2, "ask": 101.2, "depth": 480}
    ])

    # Generate CSV Output
    with open("simulation_results.csv", "w", newline="") as csvfile:
        fieldnames = [
            "Time", "OU_Process", "Jump_Diffusion", "Heston_Prices", "Heston_Vols", "ABM_Prices", "GBM_Prices", "Trade_Arrivals",
            "Bid", "Ask", "Adjusted_Size", "Sharpe_Ratio", "Sortino_Ratio", "Combined_Output", "Behavioral_Impact_Score",
            "Avg_Spread", "Avg_Depth"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for t in range(time_steps):
            writer.writerow({
                "Time": time[t],
                "OU_Process": ou_process[t],
                "Jump_Diffusion": jump_diffusion[t],
                "Heston_Prices": heston_prices[t],
                "Heston_Vols": heston_vols[t],
                "ABM_Prices": abm_prices[t],
                "GBM_Prices": gbm_prices[t],
                "Trade_Arrivals": trade_arrivals[t],
                "Bid": bid,
                "Ask": ask,
                "Adjusted_Size": adjusted_size,
                "Sharpe_Ratio": metrics["Sharpe Ratio"],
                "Sortino_Ratio": metrics["Sortino Ratio"],
                "Combined_Output": combined_output,
                "Behavioral_Impact_Score": impact_score,
                "Avg_Spread": avg_spread,
                "Avg_Depth": avg_depth
            })

    print("Simulation completed. Results saved to simulation_results.csv.")

def optimize_market_maker_objective():
    """
    Optimizes the market maker's objective function by calculating optimal quote distances.
    """
    mid_price = 100  # Example mid-price
    inventory_penalty = 0.1
    risk_aversion = 0.5

    def execution_prob_func(delta):
        """
        Example execution probability function.
        """
        return np.exp(-delta)

    optimal_distances = OrderExecution.calculate_optimal_quote_distances(
        mid_price, execution_prob_func, inventory_penalty, risk_aversion
    )

    if optimal_distances is not None and all(optimal_distances):
        delta_b, delta_a = optimal_distances
        print(f"Optimal Bid Distance: {delta_b}, Optimal Ask Distance: {delta_a}")
    else:
        print("Failed to optimize quote distances.")

# Call the optimization function
optimize_market_maker_objective()

if __name__ == "__main__":
    run_simulation()
