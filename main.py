import pandas as pd
import openpyxl as op
import twilio as tw

mouthsList = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mouth in mouthsList:
    mouthName = "database/" + mouth + ".xlsx"
    columns = pd.read_excel(mouthName)
    sellColumn = columns['Vendas']

    if(sellColumn > 55000).any():
        
        seller = columns.loc[sellColumn > 55000, 'Vendedor'].values[0]
        sell = columns.loc[sellColumn > 55000, 'Vendas'].values[0]

        print("No mês de {}, {} fez R${} em vendas!".format(mouth, seller, sell))