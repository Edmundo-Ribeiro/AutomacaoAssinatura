#   Author: Edmundo Ribeiro 
#   Email: jtvedy@gmail.com / edmundoribeiro@mecajun.com

#   Convert the google sheet data into a .json file

import pandas as pd
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


credentials_file  = 'credentials.json'
output_json_file = 'members.json'
sheet_name = 'test_sheet'

scope = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope) 

def createJsonObj(name, role, phone = '0'):
	p =  phone if type(phone) == type("0") else '0'
	f.write(f'{{\n "name":"{name}", \n "role":"{role}",\n "phone":"{p}"\n}},\n')
	

print("Authorizing...",end=" ")
try:
	gc = gspread.authorize(credentials) #Authorizing
	print("OK")

	wks = gc.open( sheet_name ).sheet1 #opening sheet

	data = wks.get_all_values() #getting the data

	df = pd.DataFrame(data) #transforming the data in a easier to use data structure


	k = df.values #getting just the values
	print(k)


	f = open(output_json_file,"w+", encoding='utf-8') #create the .json output file

	f.write("[\n")

	for name, role, phone in k:
		createJsonObj(name,role,phone)

	f.write("]")
	f.close()
	
	if not os.path.exists('Signatures'):
		os.mkdir('Signatures')

except:
	print("Error")
