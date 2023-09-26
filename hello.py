from datetime import datetime
import re
import pandas as pd

inputFileName = 'transaction_history.csv'
outputFileName = inputFileName + "_" + str(datetime.now().timestamp()) + ".csv"
amountHeader = 'Amount (total)'
headers = ['ID', 'Datetime', 'Note', 'From', 'To', amountHeader]


def moneyConverter(amount):
    newAmount = re.sub(r'^[+]*\s\$', '', amount)
    newAmount = re.sub(r'^-\s\$', '-', newAmount)
    newAmount = newAmount.strip()
    return newAmount


inputFile = pd.read_csv(inputFileName, usecols=headers,
                        converters={amountHeader: moneyConverter})

inputFile.to_csv(outputFileName, index=False)
