# Volatility Vortex Project: Optimal Market Making

## Project Summary

The Volatility Vortex project is a comprehensive framework designed to tackle the challenges of optimal market making. By simulating market dynamics, modeling execution probabilities, and optimizing quoting strategies, the project provides a robust platform for analyzing and implementing advanced market-making strategies. Below, we summarize how the project meets and exceeds the requirements outlined in `project.md`.

---

## Alignment with Project Requirements

### 1. **Mid-Price Dynamics**
- **Requirement**: Model mid-price using Arithmetic Brownian Motion (ABM) or Geometric Brownian Motion (GBM).
- **Implementation**: The project goes beyond ABM and GBM by incorporating advanced models:
  - **Ornstein-Uhlenbeck Process**: Captures mean-reverting price dynamics.
  - **Jump Diffusion Model**: Models sudden market shocks.
  - **Heston Model**: Simulates stochastic volatility.
- **Justification**: These models provide a richer and more realistic representation of market dynamics, making the analysis more robust.

### 2. **Trade Arrival & Execution Probability**
- **Requirement**: Model trade arrivals as a Poisson process and define functional forms for execution probability \( \lambda(\delta) \).
- **Implementation**:
  - Trade arrivals are modeled using a Poisson process in `advanced_order_execution.py`.
  - Functional forms for \( \lambda(\delta) \) (e.g., exponential decay) are implemented and can be extended for further research.

### 3. **Optimization Objective**
- **Requirement**: Maximize expected utility of terminal wealth or expected profit minus risk penalty, with inventory penalties.
- **Implementation**:
  - The notebook includes P&L visualizations and inventory trajectory analysis.
  - Risk penalties and utility functions are handled in `risk_management.py`.

### 4. **Simulation Approach**
- **Requirement**: Simulate mid-price paths, calculate optimal bid/ask prices, simulate trade arrivals, and update inventory and P&L.
- **Implementation**:
  - Mid-price paths are simulated in `advanced_market_simulation.py`.
  - Optimal bid/ask prices are calculated dynamically based on inventory and market conditions.
  - Trade arrivals and P&L updates are integrated into the simulation loop.

### 5. **Analysis**
- **Requirement**: Analyze terminal wealth/P&L distribution, inventory trajectories, quoted spreads, trade frequencies, and parameter sensitivity.
- **Implementation**:
  - The notebook provides detailed visualizations for all required analyses.
  - Sensitivity analysis is included to evaluate the impact of parameters like \( \gamma \) and \( \sigma \).

---

## File Overview

### 1. **`src/main.py`**
- **Purpose**: Entry point for running the simulation.
- **Key Features**:
  - Configures simulation parameters (e.g., \( \lambda \)-rate).
  - Generates `simulation_results.csv` for analysis.

### 2. **`src/executions/advanced_order_execution.py`**
- **Purpose**: Handles trade arrival simulations and execution logic.
- **Key Features**:
  - Implements Poisson-based trade arrival modeling.
  - Calculates execution probabilities based on quote distances.

### 3. **`src/simulations/advanced_market_simulation.py`**
- **Purpose**: Simulates market dynamics and mid-price paths.
- **Key Features**:
  - Supports Ornstein-Uhlenbeck, Jump Diffusion, and Heston models.
  - Provides a modular framework for adding new models.

### 4. **`src/core/risk_management.py`**
- **Purpose**: Manages risk metrics and optimization objectives.
- **Key Features**:
  - Implements risk-adjusted performance metrics (e.g., Sharpe ratio).
  - Handles inventory penalties and utility functions.

### 5. **`src/strategies/enhanced_pricing_strategy.py`**
- **Purpose**: Optimizes bid/ask quoting strategies.
- **Key Features**:
  - Dynamically adjusts quotes based on inventory and market conditions.
  - Integrates with execution and risk management modules.

### 6. **`src/utils/data_analysis.py`**
- **Purpose**: Provides tools for analyzing simulation results.
- **Key Features**:
  - Calculates P&L metrics and trade frequencies.
  - Generates visualizations for sensitivity analysis.

### 7. **`notebook/advanced_market_simulation.ipynb`**
- **Purpose**: Interactive analysis and visualization of simulation results.
- **Key Features**:
  - Visualizes mid-price dynamics, inventory trajectories, and P&L metrics.
  - Includes sensitivity analysis and parameter tuning.

### 8. **`simulation_results.csv`**
- **Purpose**: Stores simulation outputs for analysis.
- **Key Features**:
  - Contains time series data, pricing metrics, and risk metrics.

---

## Highlights

- **Advanced Models**: Incorporates state-of-the-art models for market dynamics.
- **Comprehensive Analysis**: Provides detailed insights into market-making strategies.
- **Extensibility**: Modular design allows for easy addition of new models and strategies.

> **Fun Fact**: If market-making were a video game, this project would be the "boss level"—challenging but incredibly rewarding!

---

## Conclusion

The Volatility Vortex project not only meets but exceeds the requirements outlined in `project.md`. By combining advanced modeling techniques, robust simulation frameworks, and comprehensive analysis tools, it provides a powerful platform for exploring optimal market-making strategies. Whether you're a researcher, practitioner, or just someone who loves a good stochastic process, this project has something for you.

---

## Final PnL Analysis

The final PnL (Profit and Loss) is a critical metric for evaluating the performance of the market-making strategy. Below is a summary of the PnL analysis:

### Summary Statistics
- **Mean**: Provides the average PnL across all simulations.
- **Standard Deviation**: Indicates the variability in PnL.
- **Minimum and Maximum**: Show the range of PnL values.

### Visualization
The PnL distribution is visualized as a histogram, highlighting the frequency of different PnL values. This helps in understanding the risk and reward profile of the strategy.

### Key Insights
- The PnL distribution provides insights into the profitability and risk of the market-making strategy.
- Outliers, if any, can indicate extreme market conditions or strategy inefficiencies.

> **Note**: The PnL data is directly loaded from the `simulation_results.csv` file, ensuring consistency with the simulation outputs.
