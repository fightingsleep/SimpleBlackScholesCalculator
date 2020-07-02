import math
from scipy.stats import norm

def get_call_price(spot, strike, rfr, vol, term):
    d1 = 1 / (vol * math.sqrt(term)) * (math.log(spot/strike) + (rfr + vol**2 / 2) * term)
    d2 = d1 - vol * math.sqrt(term)
    price = norm.cdf(d1) * spot - norm.cdf(d2) * math.exp(-rfr * term) * strike;
    return price

def main():
    spotPrice = float(input("Spot price (ex: $30): ").replace("$",""))
    exercisePrice = float(input("Exercise price (ex: $32.5): ").replace("$",""))
    riskFreeRate = float(input("Risk free rate (ex: 5%): ").replace("%","")) / 100
    volatility = float(input("Volatility (ex: 8.5%): ").replace("%","")) / 100
    timeToMaturity = float(input("Time to expiration in years (ex: 1.5 years): ").replace("years","").replace("year",""))
    callPrice = get_call_price(spotPrice, exercisePrice, riskFreeRate, volatility, timeToMaturity)
    print("\nCall price: ${0}".format(callPrice))

if __name__ == "__main__":
    main()