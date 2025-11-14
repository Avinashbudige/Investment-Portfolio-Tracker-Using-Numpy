"""
Investment Portfolio Tracker Using NumPy
Track and analyze a stock portfolio's performance over time.
"""

import numpy as np
from datetime import datetime, timedelta

# 1. PROBLEM STATEMENT
"""
Real-World Problem:
Investors need to track and analyze their stock portfolio's performance over time.
This includes monitoring:
- Individual stock performance (gains/losses)
- Portfolio diversification
- Risk metrics (volatility, standard deviation)
- Overall portfolio returns
- Best and worst performing stocks
- Portfolio value trends over time

This tool helps investors make informed decisions by providing comprehensive
analysis of their investment portfolio using NumPy's powerful array operations.
"""

# 2. DATA SETUP
print("=" * 70)
print("INVESTMENT PORTFOLIO TRACKER USING NUMPY")
print("=" * 70)
print()

# Create realistic sample data for a stock portfolio
# Portfolio contains 5 different stocks tracked over 30 days

# Stock information
stock_symbols = np.array(['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA'])
num_stocks = len(stock_symbols)
num_days = 30

# Initial stock prices (at the start of tracking period)
initial_prices = np.array([150.0, 2800.0, 350.0, 3300.0, 850.0])

# Number of shares owned for each stock
shares_owned = np.array([50, 10, 40, 8, 25])

# Generate realistic daily price data (using random walk model)
# Each stock has different volatility (standard deviation)
volatilities = np.array([0.02, 0.018, 0.015, 0.025, 0.035])  # Daily volatility %

# Create price matrix: rows = days, columns = stocks
np.random.seed(42)  # For reproducibility
daily_returns = np.random.normal(0.001, 1, (num_days, num_stocks)) * volatilities
daily_prices = np.zeros((num_days, num_stocks))
daily_prices[0] = initial_prices

# Generate cumulative prices using random walk
for day in range(1, num_days):
    daily_prices[day] = daily_prices[day-1] * (1 + daily_returns[day])

# Calculate initial investment
initial_investment = np.sum(initial_prices * shares_owned)

# Create date range for tracking
start_date = datetime.now() - timedelta(days=num_days-1)
dates = [start_date + timedelta(days=i) for i in range(num_days)]

print("Portfolio Overview:")
print("-" * 70)
print(f"Tracking Period: {dates[0].strftime('%Y-%m-%d')} to {dates[-1].strftime('%Y-%m-%d')}")
print(f"Number of Stocks: {num_stocks}")
print(f"Number of Trading Days: {num_days}")
print(f"Initial Investment: ${initial_investment:,.2f}")
print()

print("Stock Holdings:")
print("-" * 70)
for i, symbol in enumerate(stock_symbols):
    print(f"{symbol:6s} | Shares: {shares_owned[i]:3d} | "
          f"Initial Price: ${initial_prices[i]:8.2f} | "
          f"Initial Value: ${(initial_prices[i] * shares_owned[i]):10.2f}")
print()

# 3. ANALYSIS
print("=" * 70)
print("PORTFOLIO ANALYSIS")
print("=" * 70)
print()

# Calculate daily portfolio values
daily_portfolio_values = np.sum(daily_prices * shares_owned, axis=1)

# Calculate total returns
current_prices = daily_prices[-1]
current_portfolio_value = daily_portfolio_values[-1]
total_return = current_portfolio_value - initial_investment
total_return_pct = (total_return / initial_investment) * 100

# Calculate individual stock performance
stock_returns = current_prices - initial_prices
stock_returns_pct = (stock_returns / initial_prices) * 100
stock_values_current = current_prices * shares_owned
stock_gains = stock_returns * shares_owned

# Calculate portfolio statistics
mean_portfolio_value = np.mean(daily_portfolio_values)
max_portfolio_value = np.max(daily_portfolio_values)
min_portfolio_value = np.min(daily_portfolio_values)

# Calculate volatility (standard deviation of daily returns)
portfolio_daily_returns = np.diff(daily_portfolio_values) / daily_portfolio_values[:-1]
portfolio_volatility = np.std(portfolio_daily_returns) * 100

# Calculate stock correlations
price_changes = np.diff(daily_prices, axis=0)
correlation_matrix = np.corrcoef(price_changes.T)

# Identify best and worst performers
best_performer_idx = np.argmax(stock_returns_pct)
worst_performer_idx = np.argmin(stock_returns_pct)

# Calculate portfolio weights (diversification)
portfolio_weights = stock_values_current / current_portfolio_value * 100

# Calculate risk-adjusted metrics
sharpe_ratio = np.mean(portfolio_daily_returns) / np.std(portfolio_daily_returns) * np.sqrt(252)  # Annualized

# 4. INSIGHTS
print("Overall Portfolio Performance:")
print("-" * 70)
print(f"Initial Portfolio Value:    ${initial_investment:,.2f}")
print(f"Current Portfolio Value:    ${current_portfolio_value:,.2f}")
print(f"Total Return:               ${total_return:,.2f}")
print(f"Total Return (%):           {total_return_pct:+.2f}%")
print(f"Average Portfolio Value:    ${mean_portfolio_value:,.2f}")
print(f"Maximum Portfolio Value:    ${max_portfolio_value:,.2f}")
print(f"Minimum Portfolio Value:    ${min_portfolio_value:,.2f}")
print(f"Portfolio Volatility:       {portfolio_volatility:.2f}%")
print(f"Sharpe Ratio (Annualized):  {sharpe_ratio:.2f}")
print()

print("Individual Stock Performance:")
print("-" * 70)
print(f"{'Stock':<8} {'Initial $':<12} {'Current $':<12} {'Return $':<12} {'Return %':<10} {'Value $':<12}")
print("-" * 70)
for i, symbol in enumerate(stock_symbols):
    print(f"{symbol:<8} ${initial_prices[i]:<11.2f} ${current_prices[i]:<11.2f} "
          f"${stock_returns[i]:<11.2f} {stock_returns_pct[i]:>8.2f}% ${stock_values_current[i]:<11.2f}")
print()

print("Best & Worst Performers:")
print("-" * 70)
print(f"Best Performer:  {stock_symbols[best_performer_idx]} "
      f"({stock_returns_pct[best_performer_idx]:+.2f}% return)")
print(f"Worst Performer: {stock_symbols[worst_performer_idx]} "
      f"({stock_returns_pct[worst_performer_idx]:+.2f}% return)")
print()

print("Portfolio Diversification (Current Weights):")
print("-" * 70)
for i, symbol in enumerate(stock_symbols):
    bar_length = int(portfolio_weights[i] / 2)  # Scale for display
    bar = '█' * bar_length
    print(f"{symbol:<8} {portfolio_weights[i]:>5.1f}% {bar}")
print()

print("Stock Correlation Matrix:")
print("-" * 70)
print(f"{'':>8}", end='')
for symbol in stock_symbols:
    print(f"{symbol:>8}", end='')
print()
for i, symbol in enumerate(stock_symbols):
    print(f"{symbol:>8}", end='')
    for j in range(num_stocks):
        print(f"{correlation_matrix[i, j]:>8.2f}", end='')
    print()
print()

print("Risk Analysis:")
print("-" * 70)
stock_volatilities = np.std(np.diff(daily_prices, axis=0) / daily_prices[:-1], axis=0) * 100
for i, symbol in enumerate(stock_symbols):
    risk_level = "High" if stock_volatilities[i] > 3.0 else "Medium" if stock_volatilities[i] > 1.5 else "Low"
    print(f"{symbol:<8} Volatility: {stock_volatilities[i]:>5.2f}% | Risk Level: {risk_level}")
print()

# 5. VISUALIZATION PREP
print("=" * 70)
print("DATA PREPARED FOR VISUALIZATION")
print("=" * 70)
print()

# Prepare data structures for potential plotting
visualization_data = {
    'dates': dates,
    'daily_portfolio_values': daily_portfolio_values,
    'daily_prices': daily_prices,
    'stock_symbols': stock_symbols,
    'portfolio_weights': portfolio_weights,
    'stock_returns_pct': stock_returns_pct,
    'correlation_matrix': correlation_matrix
}

print("Available data for visualization:")
print("-" * 70)
print("1. Daily Portfolio Values (time series)")
print(f"   Shape: {daily_portfolio_values.shape}")
print("   Use: Plot portfolio value over time")
print()
print("2. Daily Stock Prices (time series)")
print(f"   Shape: {daily_prices.shape}")
print("   Use: Plot individual stock prices over time")
print()
print("3. Portfolio Weights (pie chart data)")
print(f"   Shape: {portfolio_weights.shape}")
print("   Use: Pie chart showing portfolio allocation")
print()
print("4. Stock Returns Percentage (bar chart data)")
print(f"   Shape: {stock_returns_pct.shape}")
print("   Use: Bar chart comparing stock performance")
print()
print("5. Correlation Matrix (heatmap data)")
print(f"   Shape: {correlation_matrix.shape}")
print("   Use: Heatmap showing stock correlations")
print()

# Summary statistics for export
print("Summary Statistics (NumPy Arrays Ready for Export):")
print("-" * 70)
print(f"Mean Daily Portfolio Value:  {np.mean(daily_portfolio_values):.2f}")
print(f"Median Daily Portfolio Value: {np.median(daily_portfolio_values):.2f}")
print(f"Portfolio Value Std Dev:     {np.std(daily_portfolio_values):.2f}")
print(f"Portfolio Value Range:       {np.ptp(daily_portfolio_values):.2f}")
print(f"Best Single Day Gain:        {np.max(np.diff(daily_portfolio_values)):.2f}")
print(f"Worst Single Day Loss:       {np.min(np.diff(daily_portfolio_values)):.2f}")
print()

print("=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
print()
print("Key Insights:")
print(f"✓ Your portfolio has {('gained' if total_return > 0 else 'lost')} "
      f"${abs(total_return):.2f} ({total_return_pct:+.2f}%)")
print(f"✓ Best performing stock: {stock_symbols[best_performer_idx]} "
      f"({stock_returns_pct[best_performer_idx]:+.2f}%)")
print(f"✓ Portfolio volatility is {portfolio_volatility:.2f}% "
      f"({'high' if portfolio_volatility > 2 else 'moderate' if portfolio_volatility > 1 else 'low'} risk)")
print(f"✓ Portfolio is {'well-diversified' if np.max(portfolio_weights) < 40 else 'moderately diversified' if np.max(portfolio_weights) < 60 else 'concentrated'} "
      f"(largest holding: {np.max(portfolio_weights):.1f}%)")
print()
