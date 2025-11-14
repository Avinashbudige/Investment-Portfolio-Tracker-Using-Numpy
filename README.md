# Investment Portfolio Tracker Using NumPy

A Python-based tool for tracking and analyzing stock portfolio performance over time using NumPy's powerful array operations.

## Overview

This project demonstrates how to use NumPy for financial portfolio analysis, providing insights into:
- Individual stock performance (gains/losses)
- Portfolio diversification and allocation
- Risk metrics (volatility, standard deviation)
- Overall portfolio returns
- Stock correlations
- Best and worst performing stocks
- Portfolio value trends over time

## Features

✨ **Comprehensive Analysis**
- Track multiple stocks over time
- Calculate total and individual stock returns
- Analyze portfolio volatility and risk
- Compute Sharpe ratio for risk-adjusted returns
- Generate correlation matrices between stocks

📊 **Data Visualization Preparation**
- Ready-to-use data structures for plotting
- Portfolio value time series
- Stock price histories
- Portfolio allocation weights
- Performance comparisons

🔢 **NumPy-Powered Calculations**
- Efficient array operations for large datasets
- Statistical analysis using NumPy functions
- Matrix operations for correlation analysis
- Vectorized calculations for performance

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Avinashbudige/Investment-Portfolio-Tracker-Using-Numpy.git
cd Investment-Portfolio-Tracker-Using-Numpy
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the portfolio tracker:
```bash
python portfolio_tracker.py
```

The script will:
1. Set up a sample portfolio with 5 stocks (AAPL, GOOGL, MSFT, AMZN, TSLA)
2. Generate 30 days of realistic price data
3. Perform comprehensive analysis
4. Display detailed insights and statistics
5. Prepare data for visualization

## Code Structure

The implementation follows a clear structure:

```python
# 1. PROBLEM STATEMENT
# Clear description of the real-world problem

# 2. DATA SETUP
# Create realistic sample data with context

# 3. ANALYSIS
# Apply NumPy operations with business logic

# 4. INSIGHTS
# Print meaningful results with interpretation

# 5. VISUALIZATION PREP
# Prepare data for potential plotting
```

## Sample Output

The tool provides detailed analysis including:
- Portfolio overview and holdings
- Overall performance metrics
- Individual stock performance
- Best and worst performers
- Portfolio diversification visualization
- Stock correlation matrix
- Risk analysis
- Key insights summary

## Dependencies

- Python 3.7+
- NumPy 1.21.0+

## Real-World Applications

This tool can be adapted for:
- Personal investment tracking
- Portfolio optimization analysis
- Risk management
- Investment strategy backtesting
- Educational purposes for finance and data science

## Technical Highlights

- **Random Walk Model**: Generates realistic stock price movements
- **Vectorized Operations**: Efficient NumPy calculations
- **Statistical Analysis**: Volatility, correlation, and risk metrics
- **Portfolio Theory**: Diversification and risk-adjusted returns

## Future Enhancements

Potential improvements:
- Add data visualization with matplotlib
- Import real stock data from APIs
- Implement portfolio optimization algorithms
- Add more risk metrics (VaR, Sortino ratio)
- Create interactive dashboard
- Support for multiple currencies
- Transaction history tracking

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Avinash Budige

## Acknowledgments

Built with NumPy for efficient numerical computing in Python.