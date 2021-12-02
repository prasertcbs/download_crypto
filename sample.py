# pip install pandas openpyxl investpy

import pandas as pd
import investpy as iv

def get_cryptos_historical_data(stocks, from_date, to_date):
    dfs=[]
    for stock in stocks:
        ds = iv.get_crypto_historical_data(crypto=stock,
                                           from_date=from_date, to_date=to_date)
        ds['Symbol']=stock.upper()
        ds['pct_change']=ds['Close'].pct_change()
        dfs.append(ds)
    df=pd.concat(dfs)
    return df

today=pd.Timestamp.today().date().strftime('%d/%m/%Y')
# symbols=['bitcoin', 'ethereum', 'binance coin', 'Tether']
symbols=['bitcoin', 'ethereum']
df=get_cryptos_historical_data(symbols, '01/01/2021', today)

timestamp=pd.Timestamp.today().date().strftime('%Y-%m-%d')
df.to_excel(f'cryptos_{timestamp}.xlsx')
