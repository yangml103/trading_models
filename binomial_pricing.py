import math

def binomial_option_pricing(S, K, T, r, sigma, N, option_type='call'):
    """
    Calculate the European option price using the binomial option pricing model.

    Parameters:
    - S: float, current stock price
    - K: float, strike price
    - T: float, time to maturity in years
    - r: float, risk-free interest rate (annualized)
    - sigma: float, volatility of the underlying asset (annualized)
    - N: int, number of time steps in the binomial tree
    - option_type: str, 'call' or 'put'

    Returns:
    - option_price: float, the calculated price of the option
    """
    # Calculate the time increment
    delta_t = T / N

    # Calculate up and down factors
    u = math.exp(sigma * math.sqrt(delta_t))      # Up factor
    d = 1 / u                                     # Down factor

    # Calculate risk-neutral probability
    p = (math.exp(r * delta_t) - d) / (u - d)

    # Initialize asset price and option value arrays
    asset_prices = [0.0 for _ in range(N + 1)]
    option_values = [0.0 for _ in range(N + 1)]

    # Compute asset prices at maturity
    for i in range(N + 1):
        asset_prices[i] = S * (u ** (N - i)) * (d ** i)

    # Compute option values at maturity
    for i in range(N + 1):
        if option_type == 'call':
            option_values[i] = max(0.0, asset_prices[i] - K)
        elif option_type == 'put':
            option_values[i] = max(0.0, K - asset_prices[i])
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    # Backward induction through the tree
    for j in range(N - 1, -1, -1):
        for i in range(j + 1):
            option_values[i] = (
                p * option_values[i] + (1 - p) * option_values[i + 1]
            ) * math.exp(-r * delta_t)

    return option_values[0]

# Example usage:
if __name__ == "__main__":
    S = 100.0    # Current stock price
    K = 100.0    # Strike price
    T = 1.0      # Time to maturity (1 year)
    r = 0.05     # Risk-free interest rate (5%)
    sigma = 0.2  # Volatility (20%)
    N = 50       # Number of time steps

    call_price = binomial_option_pricing(S, K, T, r, sigma, N, option_type='call')
    put_price = binomial_option_pricing(S, K, T, r, sigma, N, option_type='put')

    print(f"European Call Option Price: {call_price:.4f}")
    print(f"European Put Option Price: {put_price:.4f}")
