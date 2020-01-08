#   Autor: Edmundo Ribeiro 
#   Email: jtvedy@gmail.com / edmundoribeiro@mecajun.com

#   Código para conversão dos dados na planilha do google drive
#	para o formato .json

import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
         'arquivo-com-as-credencias-do-projeto.json', scope) # credenciais do json


def createJsonObj(name, role, phone = '0'):
	p =  phone if type(phone) == type("0") else '0'
	f.write('{\n"name": "' + name +'",\n'+ '"role": "' + role +'",\n'+ '"phone": "' + p +'"\n},\n');


print("Autorizando...",end=" ")
try:
	gc = gspread.authorize(credentials) #autorização
	print("OK")

	wks = gc.open("assinaturas-email").sheet1 #abrir planilha

	data = wks.get_all_values() #pegar dados da planilha

	df = pd.DataFrame(data) #transforma data em um dataframe
	

	k = df.values #pega os valores do dataframe
	print(k)


	f = open("membros.json","w+", encoding='utf-8') #cria o arquivo onde será salvo o json

	f.write("[\n")
	
	for name, role, phone in k:
		createJsonObj(name,role,phone)
	
	f.write("]")
	f.close()

except:
	print("Error")








# df = pd.read_excel (r'C:\Users\Edmundo\Desktop\assinaturas\assinaturas-email.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'