import yfinance as yf



#Adding function to fetch stock data from Yahoo Finance
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.cashflow.loc["Free Cash Flow"].iloc[0]



def calculate_dcf(ticker):

    #Discount logic would go here
    #1. Fetch financial data
    #2. Project future cash flows
    #3. Determine discount rate

    print(f"Calculating DCF for {ticker}...")

    starting_fcf = fetch_stock_data(ticker)
    print(f"Starting Free Cash Flow: {starting_fcf}")


    growth_rate = 0.05  #Assumed growth rate
    discount_rate = 0.10  #Assumed discount rate
    years=10


    #Calculating future cash flow value year by year
    future_cash_flows = []

    for year in range(1, years + 1):
        #Calculating FUTURE value of free cash flow
        fcf = starting_fcf * ((1 + growth_rate) ** year)

        #Calculating PRESENT value of free cash flow
        present_value = fcf / ((1 + discount_rate) ** year)

        future_cash_flows.append(present_value)
        print(f"Year {year}:Present Value: {present_value}")



    print(f"------Final Result------")

    print(f"Total Present Value of Future Cash Flows: {sum(future_cash_flows)}")

    
calculate_dcf("AAPL")









