# Data Analysis and Visualization
# This script implements tools for factor analysis, scenario analysis, and interactive dashboards.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalysis:
    @staticmethod
    def factor_analysis(data, factors):
        """
        Decomposes strategy performance into contributing factors.

        :param data: DataFrame containing performance metrics.
        :param factors: List of factor names to analyze.
        :return: Correlation matrix of factors.
        """
        correlation_matrix = data[factors].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
        plt.title("Factor Correlation Matrix")
        plt.show()
        return correlation_matrix

    @staticmethod
    def scenario_analysis(data, scenarios):
        """
        Visualizes performance under different market regimes.

        :param data: DataFrame containing performance metrics.
        :param scenarios: Dictionary mapping scenario names to filters.
        :return: None
        """
        for scenario, condition in scenarios.items():
            filtered_data = data.query(condition)
            plt.plot(filtered_data["Time"], filtered_data["OU_Process"], label=f"OU - {scenario}")
            plt.plot(filtered_data["Time"], filtered_data["Jump_Diffusion"], label=f"Jump Diffusion - {scenario}")
        plt.title("Scenario Analysis")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

    @staticmethod
    def interactive_dashboard(data):
        """
        Creates an interactive dashboard for real-time monitoring and analysis.

        :param data: DataFrame containing performance metrics.
        :return: None
        """
        try:
            import plotly.express as px
            fig = px.line(data, x="Time", y=["OU_Process", "Jump_Diffusion", "Heston_Prices"], title="Interactive Dashboard")
            fig.show()
        except ImportError:
            print("Plotly is not installed. Please install it to use the interactive dashboard.")

# Example usage (can be removed or commented out in production):
if __name__ == "__main__":
    # Load example data
    data = pd.read_csv("../simulation_results.csv")

    # Factor Analysis Example
    factors = ["OU_Process", "Jump_Diffusion", "Heston_Prices"]
    DataAnalysis.factor_analysis(data, factors)

    # Scenario Analysis Example
    scenarios = {
        "High Volatility": "Heston_Vols > 0.05",
        "Low Volatility": "Heston_Vols <= 0.05"
    }
    DataAnalysis.scenario_analysis(data, scenarios)

    # Interactive Dashboard Example
    DataAnalysis.interactive_dashboard(data)
