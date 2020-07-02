import math
from scipy.stats import norm

def get_call_price(spot, strike, rfr, vol, term):
    d1 = 1 / (vol * math.sqrt(term)) * (math.log(spot/strike) + (rfr + vol**2 / 2) * term)
    d2 = d1 - vol * math.sqrt(term)
    price = norm.cdf(d1) * spot - norm.cdf(d2) * math.exp(-rfr * term) * strike;
    return price

def main():
    spotPrice = float(input("Spot price: "))
    exercisePrice = float(input("Exercise price: "))
    riskFreeRate = float(input("Risk free rate: "))
    volatility = float(input("Volatility: "))
    timeToMaturity = float(input("Term (years): "))
    print(get_call_price(spotPrice, exercisePrice, riskFreeRate, volatility, timeToMaturity))

if __name__ == "__main__":
    main()