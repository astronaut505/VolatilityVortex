# Volatility Vortex Project

## Overview

The Volatility Vortex project is a comprehensive framework for implementing and analyzing market-making strategies. It is designed to simulate various market conditions, pricing strategies, and order execution methods, making it an ideal foundation for research in Quantitative Finance. The project combines theoretical rigor with practical implementation, providing tools for advanced market simulation, risk management, and extensibility for further research.

## Key Features

### 1. **Market Simulation**

The project includes advanced market simulation models to mimic real-world market dynamics:

- **Ornstein-Uhlenbeck Process (Mean-Reverting)**: Simulates mean-reverting price dynamics, often used for modeling interest rates or mean-reverting assets.
- **Jump Diffusion Model**: Introduces sudden price jumps to mimic market shocks, useful for modeling assets with discontinuous price changes.
- **Heston Model (Stochastic Volatility)**: Simulates time-varying volatility, commonly used for option pricing and risk management.

> **Note**: Arithmetic Brownian Motion (ABM) and Geometric Brownian Motion (GBM) are not explicitly used in this project. Instead, the focus is on more advanced models like the ones listed above.

### 2. **Pricing Strategies**

- **Machine Learning-Based Strategies**: Predicts optimal bid/ask spreads using historical data.
- **Reinforcement Learning**: Optimizes trading decisions using Q-learning.

### 3. **Order Execution**

- **Adaptive Execution Algorithms**: Adjusts order sizes and timing based on market conditions.
- **Market Impact Models**: Accounts for price slippage due to large orders.
- **Latency Arbitrage**: Explores strategies exploiting differences in market latency.

### 4. **Risk Management**

- **Dynamic Hedging**: Adjusts hedge positions dynamically based on portfolio and derivative values.
- **Stress Testing**: Simulates extreme market scenarios to evaluate strategy robustness.
- **Risk-Adjusted Metrics**: Calculates Sharpe and Sortino ratios for performance evaluation.

### 5. **Data Analysis and Visualization**

- **Factor Analysis**: Decomposes strategy performance into contributing factors.
- **Scenario Analysis**: Visualizes performance under different market regimes.
- **Interactive Dashboards**: Provides real-time monitoring and analysis.

### 6. **Extensibility for Research**

- **Hybrid Models**: Combines traditional financial models with machine learning outputs.
- **Behavioral Finance**: Analyzes the impact of trader psychology on market dynamics.
- **Market Microstructure**: Studies the impact of order book dynamics on strategy performance.

## Outputs

The project generates a CSV file (`simulation_results.csv`) containing the following data:

- **Time Series Data**: Outputs from market simulation models (e.g., Ornstein-Uhlenbeck, Jump Diffusion, Heston).
- **Pricing Metrics**: Bid/ask spreads and adjusted order sizes.
- **Risk Metrics**: Sharpe and Sortino ratios.
- **Extensibility Metrics**: Hybrid model outputs, behavioral impact scores, and market microstructure analysis results.

## Final Result

The final result is a comprehensive analysis of market-making strategies under various simulated conditions. The notebook (`notebook/advanced_market_simulation.ipynb`) visualizes the results, including:

- Plots of market simulation models.
- Risk-adjusted performance metrics.
- Demonstrations of extensibility features (e.g., hybrid models, behavioral analysis).

## How to Use

1. **Run the Simulation**:

   - Execute `main.py` in the `src/` directory to generate the `simulation_results.csv` file.
     ```bash
     python src/main.py
     ```

2. **Analyze Results**:

   - Open the notebook (`notebook/advanced_market_simulation.ipynb`) to visualize and analyze the results.

3. **Extend the Project**:
   - Use the modular design to add new models, strategies, or analysis tools.

## Models Used and Their Purpose

- **Ornstein-Uhlenbeck Process**: Models mean-reverting assets, useful for interest rates or commodities.
- **Jump Diffusion Model**: Captures sudden market shocks, ideal for assets with discontinuous price changes.
- **Heston Model**: Simulates stochastic volatility, widely used in option pricing and risk management.

This project provides a robust framework for studying and implementing market-making strategies, making it a valuable tool for both academic research and practical applications.

Note: Arithmetic Brownian Motion (ABM) and Geometric Brownian Motion (GBM) are not used in this project. Instead, we focused on more advanced models like Ornstein-Uhlenbeck, Jump Diffusion, and Heston.
