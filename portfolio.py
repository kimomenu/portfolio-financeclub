import pandas_datareader.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


#actual date for output graph
enddate="2017-06-05" 

#fetch data from portfolio excel file
portfolio_table=pd.read_excel("portfolio.xlsx",sheetname=0)
portfolio_table.head()

#definition of tickers and dates lists, IMPROVEMENT, consult from portfolio dataframe directly
names=portfolio_table['name'].astype(str).values.tolist()
tickers=portfolio_table['ticker'].astype(str).values.tolist()
dates=portfolio_table['date'].astype(str).values.tolist()
nshares=portfolio_table['shares'].astype(int).values.tolist()
scurrency=portfolio_table['currency'].astype(str).values.tolist()
tsource=portfolio_table['source'].astype(str).values.tolist()

#definition of portfolio dictionary
df=dict()
base_currency= "CHF"

#data fetch from google finance, some tickers don't work, HKG:0699 and AMS:MT, SWX:SPSN
for i in range(0,len(tickers)):
    df[i] = web.DataReader(tickers[i], 'google', dates[i], enddate)
    value=df[i].iat[0,3]
    df[i]['Index']=100*df[i]['Close']/value
    #print tickers[i]
    df[i].to_csv(r'%s.txt'%(names[i]),sep=' ', index=False, header=True)
print df[5]



position=pd.DataFrame(index=tickers,columns=['buy_value','today_value','today_cgain'])
#print position

#calculation of portfolio position, query of forex rates for today and buy date for each stock
for i in range(0,len(tickers)):
    forex_today= pd.read_json('http://api.fixer.io/%s?base=CHF'%(enddate))
    forex_buy=pd.read_json('http://api.fixer.io/%s?base=CHF'%(dates[i]))
    forex_today.head()
    forex_buy.head()
    position.loc[tickers[i],'buy_value']=nshares[i]*df[i]['Close'].iloc[0]/forex_buy.loc[scurrency[i],'rates']
    print position
    position.loc[tickers[i],'today_value']=nshares[i]*df[i]['Close'].iloc[-1]/forex_today.loc[scurrency[i],'rates']
    if nshares[i]>0:
        position.loc[tickers[i],'today_cgain']=position.loc[tickers[i],'today_value']-position.loc[tickers[i],'buy_value']

print pd.read_json('http://api.fixer.io/%s?base=CHF'%(enddate))
print position

#plot figure declaration
    
fig=plt.figure(figsize=(20,10), dpi=150)

#plot loop
for i in range(0,len(tickers)):
    plt.plot(df[i]['Index'],label=tickers[i])
plt.legend()
plt.axhline(y=100, color='k', linestyle='dashed')
#plot save in png file

save_file = "portfolio.png"
plt.savefig(save_file)
plt.close(fig)



