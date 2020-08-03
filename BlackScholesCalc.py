import math
from scipy.stats import norm

# This method calculates the value of a European call option using Black Scholes
# args:
#   spot - The current spot price of the stock
#   strike - The strike price of the call option
#   rfr- The risk free interest rate
#   vol - The volatility of the stock price
#   term - The term to maturity of the option (in years)
def get_call_price(spot, strike, rfr, vol, term):
    d1 = 1 / (vol * math.sqrt(term)) * (math.log(spot/strike) + (rfr + vol**2 / 2) * term)
    d2 = d1 - vol * math.sqrt(term)
    return norm.cdf(d1) * spot - norm.cdf(d2) * strike * math.exp(-rfr * term);

# This method calculates the value of a European put option using Black Scholes
# args:
#   spot - The current spot price of the stock
#   strike - The strike price of the put option
#   rfr- The risk free interest rate
#   vol - The volatility of the stock price
#   term - The term to maturity of the option (in years)
def get_put_price(spot, strike, rfr, vol, term):
    d1 = 1 / (vol * math.sqrt(term)) * (math.log(spot/strike) + (rfr + vol**2 / 2) * term)
    d2 = d1 - vol * math.sqrt(term)
    return norm.cdf(-d2) * strike * math.exp(-rfr * term) - norm.cdf(-d1) * spot;

def main():
    # Gather the inputs from the user
    spot_price = float(input("Spot price (ex: $30): ").replace("$",""))
    exercise_price = float(input("Exercise price (ex: $32.5): ").replace("$",""))
    risk_free_rate = float(input("Risk free rate (ex: 5%): ").replace("%","")) / 100
    volatility = float(input("Volatility (ex: 20%): ").replace("%","")) / 100
    time_to_maturity = float(input("Time to expiration in years (ex: 1.5 years): ").replace("years","").replace("year",""))

    # Calculate the value of a call and put option based on the inputs
    call_price = get_call_price(spot_price, exercise_price, risk_free_rate, volatility, time_to_maturity)
    put_price = get_put_price(spot_price, exercise_price, risk_free_rate, volatility, time_to_maturity)

    # Print the option values
    print("\nCall price: ${0}".format(call_price))
    print("\nPut price: ${0}".format(put_price))

if __name__ == "__main__":
    main()