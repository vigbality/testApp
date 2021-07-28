import gspread
from oauth2client.service_account import ServiceAccountCredentials

try:
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

	creds = ServiceAccountCredentials.from_json_keyfile_name("testapp-6d21738b9b56.json", scope)

	client = gspread.authorize(creds)
	dataFile = client.open("dataFile")
	resultData = client.open("resultData")
	availableTests=client.open('availableTests')



except:
    pass

def vacantRow(worksheet):
	values_list = worksheet.col_values(1)
	return len(values_list)+1		

# dataFile>>         https://docs.google.com/spreadsheets/d/1wpEz-ECPboXSLcn_J3FexwTPRaYr9A2G_XjuZJ86QRI/edit#gid=6111950
# resultData>>       https://docs.google.com/spreadsheets/d/1liN80NYCWXxj3g71EIZ4FbxmlscNGtYgo6fJZsGa7eU/edit#gid=1488749677
# availableTests>>   https://docs.google.com/spreadsheets/d/1P8LYlrEP1nNNCx7-Rdh6QO5FVNHFm5CobBdpRnF3lQo/edit#gid=1790742163
# mainPageLogin      https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fu%2F0%2F&followup=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fu%2F0%2F&ltmpl=sheets&flowName=GlifWebSignIn&flowEntry=ServiceLogin