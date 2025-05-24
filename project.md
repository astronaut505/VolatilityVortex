# Final Project Overview & Requirements

## Project List

- **Project 1**: Estimating Effective Spreads
- **Project 2**: Information Asymmetry & Price Discovery
- **Project 3**: Optimal Market Making
- **Project 4**: Alternative Trading Mechanisms
- **Project 5**: Decomposing the Bid-Ask Spread

---

## 📌 Project 3: Optimal Market Making

### 🎯 Goal

To derive and analyze the **optimal quoting strategy** (bid and ask prices) for a market maker who faces:

- Inventory risk due to stochastic price movements
- Execution risk due to uncertainty about whether their quotes will be hit

---

## 🔍 Core Question

> Given a model for mid-price evolution and a functional form for trade execution probability depending on quote distance from the mid-price, what are the **optimal bid and ask quote distances** \((\delta_b^_, \delta_a^_)\) that **maximize the market maker’s objective function** (e.g., balancing profit and risk)?

---

## 📈 Modeling the Market Maker’s Problem

### 🧮 Mid-Price Dynamics \((S_t)\)

The mid-price is modeled as a **stochastic process**:

#### Option 1: Arithmetic Brownian Motion (ABM)

- Continuous: \( dS_t = \mu dt + \sigma dW_t \)
- Discrete: \( S*t = S*{t-1} + \epsilon_t \)
- ✅ Simpler math, common in inventory models
- ❌ Allows negative prices; non-stationary percentage returns

#### Option 2: Geometric Brownian Motion (GBM)

- Often more realistic due to always-positive prices
- Preferred in financial modeling for assets

#### Task:

- Select either ABM or GBM
- Define and justify parameters \( \mu, \sigma \)

---

## ⚙️ Trade Arrival & Execution Probability \((\lambda(\delta))\)

### 💡 Execution Modeling

- Market orders arrive randomly, modeled by a **Poisson process**
- Arrival intensity \( \lambda \) depends on quote distance \( \delta \) from mid-price

### Quote Distance Definitions:

- Bid: \( \delta_b = S_t - p_b \)
- Ask: \( \delta_a = p_a - S_t \)

### Functional Forms for \( \lambda(\delta) \):

| Form              | Formula                                           | Description                      |
| ----------------- | ------------------------------------------------- | -------------------------------- |
| Exponential Decay | \( \lambda(\delta) = A e^{-k \delta} \)           | Used in Avellaneda-Stoikov model |
| Linear Decay      | \( \lambda(\delta) = \max(A - k\delta, 0) \)      | Simple cut-off style             |
| Power Law         | \( \lambda(\delta) = A(\delta + \epsilon)^{-k} \) | More flexible decay              |

---

## 📊 Optimization Objective

### 🎯 Market Maker’s Goals:

1. **Maximize Expected Utility of Terminal Wealth**

   - Use exponential utility: \( U(W) = -e^{-\gamma W} \)
   - Risk aversion parameter \( \gamma \)

2. **Maximize Expected Profit Minus Risk Penalty**

   - Objective: \( \mathbb{E}[P\&L] - \phi \cdot \text{Var}(P\&L) \)

3. **Inventory Penalty**
   - Penalize large inventories:
     \( \text{Objective term: } -\kappa q_t^2 \)

### 📉 Key Trade-Off:

- **Wider spread**: ↑ profit per trade, ↓ trade frequency
- **Narrower spread**: ↑ frequency, ↑ inventory risk

---

## 🧪 Simulation Approach

### 🎯 Goal

Evaluate performance of optimal quoting strategy \( (\delta_b^_, \delta_a^_) \)

### 🛠️ Steps

1. **Simulate** mid-price paths \( S_t \) (e.g., using GBM)
2. **At each time step \( \Delta t \)**:

   - Calculate optimal bid/ask prices:
     - \( p_b^_ = S_t - \delta_b^_(t, S_t, q_t) \)
     - \( p_a^_ = S_t + \delta_a^_(t, S_t, q_t) \)

3. **Simulate trade arrivals**:

   - Probability of trade in \( \Delta t \):
     - Buy (ask hit): \( \lambda_a(\delta_a^\*) \cdot \Delta t \)
     - Sell (bid hit): \( \lambda_b(\delta_b^\*) \cdot \Delta t \)

4. **Update**:

   - Inventory \( q_t \)
   - P&L (cash)

5. **Repeat** for simulation horizon \( T \)

6. **Run Monte Carlo simulations**

---

## 📊 Analysis

- Distribution of terminal wealth / P&L
- Inventory trajectories
- Average quoted spreads
- Trade frequencies
- Sensitivity to parameters: \( \gamma \), \( \sigma \), etc.

---

**Instructor:** Bartosz Bieganowski
**Course:** Automatic Transactional Systems – Final Projects
