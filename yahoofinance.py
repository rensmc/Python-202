import csv
import yfinance as yf

def get_company_officers(ticker):
    try:
        stock = yf.Ticker(ticker)
        company_officers = stock.info.get("companyOfficers", [])
        if not company_officers:
            return []
        officers_list = []
        for officer in company_officers[:3]:
            officers_list.extend([officer["name"], officer["title"]])
        return officers_list
    except:
        return []

with open("stock_tickers.csv") as file:
    reader = csv.reader(file)
    next(reader)  # skip header row
    rows = []
    for row in reader:
        ticker = row[0]
        print(f"Processing {ticker}...")
        officers = get_company_officers(ticker)
        website = yf.Ticker(ticker).info.get('website', '')
        company = yf.Ticker(ticker).info.get('shortName', '')
        row_data = [ticker, company, website] + officers
        rows.append(row_data)

with open("company_officers_3000.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker", "Company", "Website", "Name1", "Title1", "Name2", "Title2", "Name3", "Title3"])
    writer.writerows(rows)
