import pandas as pd
import openpyxl as op
from twilio.rest import Client

account_sid = "ACc6bbdd588bb30e1c81b68e8aa95c659c"
auth_token = "69792ae172842a10d1172990d8c4fe59"
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