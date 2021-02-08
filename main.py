import pandas as pd
import openpyxl as op
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

mouthsList = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mouth in mouthsList:
    mouthName = "database/" + mouth + ".xlsx"
    columns = pd.read_excel(mouthName)
    sellColumn = columns['Vendas']

    if(sellColumn > 55000).any():
        
        seller = columns.loc[sellColumn > 55000, 'Vendedor'].values[0]
        sell = columns.loc[sellColumn > 55000, 'Vendas'].values[0]

        print("No mês de {}, {} fez R${} em vendas!".format(mouth, seller, sell))

        message = client.messages.create(
            to="+5518996220090",
            from_="+17474002884",
            body="No mês de {}, {} fez R${} em vendas!".format(mouth, seller, sell)
        )

        print(message.sid)