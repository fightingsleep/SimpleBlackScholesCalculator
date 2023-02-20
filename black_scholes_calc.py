from decimal import Decimal
import mpmath

def get_call_price(spot, strike, rfr, vol, term):
    """This method calculates the value of a European call option using Black Scholes

    Args:
        spot (Decimal): The current spot price of the stock
        strike (Decimal): The strike price of the call option
        rfr (Decimal): The risk free interest rate
        vol (Decimal): The volatility of the stock price
        term (Decimal): The term to maturity of the option (in years)

    Returns:
        Decimal: The price of the call option
    """
    d1 = Decimal('1') / (vol * term.sqrt()) * ((spot/strike).ln() + (rfr + vol ** Decimal('2') / Decimal('2')) * term)
    d2 = d1 - vol * term.sqrt()
    return mpmath.ncdf(d1) * spot - mpmath.ncdf(d2) * strike * (-rfr * term).exp()

def get_put_price(spot, strike, rfr, vol, term):
    """This method calculates the value of a European put option using Black Scholes

    Args:
        spot (Decimal): The current spot price of the stock
        strike (Decimal): The strike price of the put option
        rfr (Decimal): The risk free interest rate
        vol (Decimal): The volatility of the stock price
        term (Decimal): The term to maturity of the option (in years)

    Returns:
        Decimal: The price of the put option
    """
    d1 = Decimal('1') / (vol * term.sqrt()) * ((spot/strike).ln() + (rfr + vol ** Decimal('2') / Decimal('2')) * term)
    d2 = d1 - vol * term.sqrt()
    return mpmath.ncdf(-d2) * strike * (-rfr * term).exp() - mpmath.ncdf(-d1) * spot

def main():
    # Gather the inputs from the user
    spot_price = Decimal(input("Spot price (ex: $30): ").replace("$",""))
    exercise_price = Decimal(input("Exercise price (ex: $32.5): ").replace("$",""))
    risk_free_rate = Decimal(input("Risk free rate (ex: 5%): ").replace("%","")) / Decimal('100')
    volatility = Decimal(input("Volatility (ex: 20%): ").replace("%","")) / Decimal('100')
    time_to_maturity = Decimal(input("Time to expiration in years (ex: 1.5 years): ").replace("years","").replace("year",""))

    # Calculate the value of a call and put option based on the inputs
    call_price = get_call_price(spot_price, exercise_price, risk_free_rate, volatility, time_to_maturity)
    put_price = get_put_price(spot_price, exercise_price, risk_free_rate, volatility, time_to_maturity)

    # Print the option values
    print(f"\nCall price: ${call_price}\nPut price: ${put_price}\n")

if __name__ == "__main__":
    main()
