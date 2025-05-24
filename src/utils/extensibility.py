# Extensibility for Research
# This script provides tools for extending the project with hybrid models, behavioral finance, and market microstructure analysis.

import numpy as np

class Extensibility:
    @staticmethod
    def hybrid_model(traditional_model_output, ml_model_output, weight):
        """
        Combines traditional financial models with machine learning outputs.

        :param traditional_model_output: Output from a traditional financial model.
        :param ml_model_output: Output from a machine learning model.
        :param weight: Weight assigned to the machine learning model.
        :return: Combined output.
        """
        combined_output = (1 - weight) * traditional_model_output + weight * ml_model_output
        return combined_output

    @staticmethod
    def behavioral_analysis(trader_actions, market_conditions):
        """
        Analyzes the impact of trader psychology on market dynamics.

        :param trader_actions: Array of trader actions.
        :param market_conditions: Array of market conditions.
        :return: Behavioral impact score.
        """
        impact_score = np.corrcoef(trader_actions, market_conditions)[0, 1]
        return impact_score

    @staticmethod
    def microstructure_analysis(order_book_data):
        """
        Analyzes the impact of order book dynamics on strategy performance.

        :param order_book_data: Array of order book snapshots.
        :return: Average spread and depth.
        """
        spreads = [snapshot["ask"] - snapshot["bid"] for snapshot in order_book_data]
        depths = [snapshot["depth"] for snapshot in order_book_data]
        avg_spread = np.mean(spreads)
        avg_depth = np.mean(depths)
        return avg_spread, avg_depth

# Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    # Hybrid Model Example
    traditional_output = 0.05
    ml_output = 0.08
    weight = 0.6
    combined = Extensibility.hybrid_model(traditional_output, ml_output, weight)
    print(f"Combined Output: {combined}")

    # Behavioral Analysis Example
    trader_actions = np.array([1, -1, 1, 1, -1])
    market_conditions = np.array([0.5, -0.2, 0.3, 0.4, -0.1])
    impact_score = Extensibility.behavioral_analysis(trader_actions, market_conditions)
    print(f"Behavioral Impact Score: {impact_score}")

    # Microstructure Analysis Example
    order_book_data = [
        {"bid": 100, "ask": 101, "depth": 500},
        {"bid": 99.5, "ask": 100.5, "depth": 450},
        {"bid": 100.2, "ask": 101.2, "depth": 480}
    ]
    avg_spread, avg_depth = Extensibility.microstructure_analysis(order_book_data)
    print(f"Average Spread: {avg_spread}, Average Depth: {avg_depth}")
