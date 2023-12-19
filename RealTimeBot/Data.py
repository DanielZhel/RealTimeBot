import datetime

import httpx
from OKXAPI.MarketData import MarketAPI
import pandas as pd

def get_instrument_data (instId, bar, limit):
    timeout = httpx.Timeout(10.0, read=None)
    response = httpx.get(url="https://www.okx.com", verify=False, timeout=timeout)
    market_data = MarketAPI(flag="0", domain="https://www.okx.com", debug = True)
    cs = market_data.get_candlesticks(instId= instId,bar=bar, limit=limit)
    hist= []
    i= 0
    while i<limit:
        ts  = float(cs["data"][i][0])/1000
        time = datetime.datetime.fromtimestamp(ts)
        op = float((cs["data"])[i][1])
        hi = float((cs["data"])[i][2])
        lo = float((cs["data"])[i][3])
        cl = float((cs["data"])[i][4])
        a = {"time":time, "open":op, "high":hi, "low":lo,  "close":cl}
        hist.append(a) 
        
        i = i+1
    
    hist.reverse()
    inst_data= pd.DataFrame(hist)
    print("dd")
    return inst_data




