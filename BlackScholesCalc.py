import math
from scipy.stats import norm

def get_call_price(spot, strike, rfr, vol, term):
    d1 = 1 / (vol * math.sqrt(term)) * (math.log(spot/strike) + (rfr + vol**2 / 2) * term)
    d2 = d1 - vol * math.sqrt(term)
    return norm.cdf(d1) * spot - norm.cdf(d2) * math.exp(-rfr * term) * strike;

def main():
    spot_price = float(input("Spot price (ex: $30): ").replace("$",""))
    exercise_price = float(input("Exercise price (ex: $32.5): ").replace("$",""))
    risk_free_rate = float(input("Risk free rate (ex: 5%): ").replace("%","")) / 100
    volatility = float(input("Volatility (ex: 8.5%): ").replace("%","")) / 100
    time_to_maturity = float(input("Time to expiration in years (ex: 1.5 years): ").replace("years","").replace("year",""))
    call_price = get_call_price(spot_price, exercise_price, risk_free_rate, volatility, time_to_maturity)
    print("\nCall price: ${0}".format(call_price))

if __name__ == "__main__":
    main()