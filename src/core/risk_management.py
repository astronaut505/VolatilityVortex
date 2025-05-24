# Risk Management and Metrics
# This script implements risk management techniques, including dynamic hedging, stress testing, and risk-adjusted performance metrics.

import numpy as np

class RiskManagement:
    @staticmethod
    def dynamic_hedging(portfolio_value, derivative_value, hedge_ratio):
        """
        Adjusts the hedge position dynamically based on portfolio and derivative values.

        :param portfolio_value: Current value of the portfolio.
        :param derivative_value: Current value of the derivative.
        :param hedge_ratio: Hedge ratio to maintain.
        :return: Adjusted hedge position.
        """
        hedge_position = hedge_ratio * (portfolio_value / derivative_value)
        return hedge_position

    @staticmethod
    def stress_testing(portfolio_values, stress_scenarios):
        """
        Simulates extreme market scenarios to evaluate portfolio robustness.

        :param portfolio_values: Array of portfolio values.
        :param stress_scenarios: Array of stress scenario multipliers.
        :return: Array of stressed portfolio values.
        """
        stressed_values = [portfolio_values * scenario for scenario in stress_scenarios]
        return stressed_values

    @staticmethod
    def risk_adjusted_metrics(returns, risk_free_rate):
        """
        Calculates risk-adjusted performance metrics like Sharpe and Sortino ratios.

        :param returns: Array of portfolio returns.
        :param risk_free_rate: Risk-free rate of return.
        :return: Dictionary of risk-adjusted metrics.
        """
        excess_returns = returns - risk_free_rate
        sharpe_ratio = np.mean(excess_returns) / np.std(excess_returns)
        downside_risk = np.std([r for r in excess_returns if r < 0])
        sortino_ratio = np.mean(excess_returns) / downside_risk if downside_risk > 0 else np.inf
        return {"Sharpe Ratio": sharpe_ratio, "Sortino Ratio": sortino_ratio}

# Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    # Dynamic Hedging Example
    hedge_position = RiskManagement.dynamic_hedging(portfolio_value=100000, derivative_value=50000, hedge_ratio=0.8)
    print(f"Hedge Position: {hedge_position}")

    # Stress Testing Example
    portfolio_values = np.array([100000, 105000, 110000])
    stress_scenarios = [0.8, 0.9, 1.1]
    stressed_values = RiskManagement.stress_testing(portfolio_values, stress_scenarios)
    print(f"Stressed Portfolio Values: {stressed_values}")

    # Risk-Adjusted Metrics Example
    returns = np.array([0.02, 0.03, -0.01, 0.04])
    risk_free_rate = 0.01
    metrics = RiskManagement.risk_adjusted_metrics(returns, risk_free_rate)
    print(f"Risk-Adjusted Metrics: {metrics}")
