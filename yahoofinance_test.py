import yfinance as yf

def get_company_officers(ticker):
    try:
        stock = yf.Ticker(ticker)
        company_officers = stock.info["companyOfficers"]
        for officer in company_officers[:3]:
            print(officer["name"], officer["title"])
    except:
        print(f"No company officers found for {ticker}")

ticker = input("Enter stock ticker: ")
get_company_officers(ticker)
