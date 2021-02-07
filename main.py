import pandas as pd
import openpyxl as op
import twilio as tw

mouthsList = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mouth in mouthsList:
    mouthName = "database/" + mouth + ".xlsx"
    print(mouthName)
