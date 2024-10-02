import numpy as np
from scipy.stats import norm

def bachelier_option_price(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the price of a European option using the Bachelier model.

    NOTE: CAN HANDLE NEGATIVE ASSET VALUES
    
    Parameters:
    - S (float): Current spot price of the underlying asset
    - K (float): Strike price of the option
    - T (float): Time to maturity in years
    - r (float): Risk-free interest rate (annualized)
    - sigma (float): Volatility of the underlying asset (standard deviation of price)
    - option_type (str): 'call' or 'put'

    Returns:
    - price (float): The price of the option
    """
    # Present value of the strike price
    K_pv = K * np.exp(-r * T)
    
    # Calculate d
    d = (S - K_pv) / (sigma * np.sqrt(T))
    
    # Calculate option price
    if option_type == 'call':
        price = (S - K_pv) * norm.cdf(d) + sigma * np.sqrt(T) * norm.pdf(d)
    elif option_type == 'put':
        price = (K_pv - S) * norm.cdf(-d) + sigma * np.sqrt(T) * norm.pdf(d)
    else:
        raise ValueError("Invalid option_type. Expected 'call' or 'put'.")
    
    return price


S = 100        # Current spot price
K = 100        # Strike price
T = 1          # Time to maturity (1 year)
r = 0.05       # Risk-free interest rate (5%)
sigma = 20     # Volatility (standard deviation of price)
option_type = 'call'  # Type of the option

price = bachelier_option_price(S, K, T, r, sigma, option_type)
print(f"The price of the {option_type} option is: {price:.2f}")