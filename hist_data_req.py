import requests
import pandas
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
from datetime import datetime
import iexfinance
start = datetime(2017, 1, 15)
end = datetime(2017, 7, 10)

IEX_TOKEN = "pk_2101bab5b00b4b21aefe6ad29f6e1bf6"
output = open("C:/Users/User/Desktop/Hackathons/CalHacks6.0/CalHacks6.0MLPortfoli0-master/hist_data_raw.txt", 'w')



symbols = ["ccl", "ll", "ulta","chkp","mo","crm","RL","NTAP","GIB","MXIM","MA","TGT","AZO","BBY","LULU","TIF","NFLX", "TSLA", "STZ","VECO",
"RCL","CBS.A","PG","ADTN","STX","GRPN","CMCSA","payx","gps","Flex","Flt","jnpr","tsco","bbby","hsy","ODP","GM","CLX","ODP","IPG",
"APH","PVH", "ROST","PVH", "ADS", "Vmw","ROST","COST","FLIR","DKS","EXPE","KLAC","FSLR","ADS","ULTI","KO","WMT","INFN","K","GPN","ARW","CNK","ADM",
"SYMC","CL","KR","ADP","ZNGA","NTAP","DIS","ROST","TAP","INTU","AKAM","MGA","IBM","TJX",
"KMB","FisV","GLW","WDC","CSOD","EBAY","GRMN","RL"]

exception_counter = 0
for i in symbols:
	#current = Stock(i, token=IEX_TOKEN)
	try:
		data = get_historical_data(i, start, end,close_only=True, output_format='pandas', token = IEX_TOKEN)
		output.write("ticker:" + i)
		output.write(data.to_string())
	except:
		exception_counter += 1
		print("\n--------------------------------\nEXCEPTION THROWN!\nSYMBOL = " + str(i) + "\nTOTAL EXCEPTIONS: " + str(exception_counter) + "\n--------------------------------\n")
		pass

#data = iexfinance.stocks.get_historical_data(symbols, start, end, close_only=True, token=IEX_TOKEN, output_format='pandas')

#output.write(data.to_string())

#aapl.get_historical_prices()

#print(f.loc["2017-02-09"])

#API_ENDPOINT = "https://cloud.iexapis.com/v1//stock/{symbol}/chart/{range}/{date}?token=pk_7deb509abb794cba9329b4128f787bcd"

#GET /stock/{symbol}/chart/{range}/{date}
"""

data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 

#r = requests.get(url = API_ENDPOINT, data = data) 


#pastebin_url = r.text 
#print("The pastebin URL is:%s"%pastebin_url) 
"""










#rhuihjrefuiasdjfudsjofjdsa
#mnfjdijdk382