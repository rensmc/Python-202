import yfinance as yf

def get_company_officers(ticker):
    try:
        stock = yf.Ticker(ticker)

        print("Company: " + stock.info.get('shortName', ''))
        print("Website: " + stock.info.get('website', ''))
        print("Sector: " + stock.info.get('sector', ''))
        print("Market Cap: " + str(stock.info.get('marketCap', '')))
        
        company_officers = stock.info["companyOfficers"]
        for officer in company_officers[:4]:
            print(officer["name"], officer["title"])
    except:
        print(f"No company officers found for {ticker}")

ticker = input("Enter stock ticker: ")
get_company_officers(ticker)
