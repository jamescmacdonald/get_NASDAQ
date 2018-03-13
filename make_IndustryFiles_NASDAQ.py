
#author: JMacD
''' This creates the industry files from Nasdaq company list '''
import os
import numpy as np
import pandas as pd

# C:\Users\Jim\Downloads\StockHist

#Barchart columns
# 'symbol','timestamp','tradingDay','open','high','low','close','volume','openInterest'

path1 = r'C:\Users\Jim\Documents\StockHist' 
pathI = r'C:\Users\Jim\Documents\StockHist\industryFiles_NASDAQ'
pathD = r'C:\Users\Jim\Documents\StockHist\data_files\daily'
#pathW = r'C:\Users\Jim\Documents\StockHist\data_files\weekly'

companyFile = 'NASDAQ_CompanyLists_Quotes.csv'
indFile = 'NASDAQ_indGroups.csv' ## col = 'indGroup'

dfC = pd.read_csv(companyFile, index_col=0) ## index is 0-n
dfI = pd.read_csv(indFile, index_col=0) ## index is 0-n
print(dfI.head(2))


numInd = len(dfI)
print('# of industries = ', numInd)

# calcColumns = np.array(dfCalcCol.columns)

## function to create dataframe object
def makeDF(dfName):
	df = pd.DataFrame()
	df.name = dfName
	return df

## create list to hold short names
indShortNames = []
## Create industry files
## 
for c in range(0, 3): #numInd):
	indName = dfI.loc[c,'indGroup']
	print(indName)
	#create industry short name
	sn = indName[:9] + '_' + str(c)
	
	## filename to save at end
	fileName = sn + '.csv'

	## add name to the list
	indShortNames.append(sn)

	## write the list to file of industry short names
	with open('indShortNames_NASDAQ.txt', 'w') as cf:
 		for line in indShortNames:
 			cf.write(line + "\n")
	
	## Make new df for each industry short name
	dfXX = makeDF(sn)
	print(dfXX.name)

	## Filter the company list by Industry
	## new df holds industry symbols
	dfXX = dfC[(dfC['indGroup'] == indName) ]
	
	## this would create this row
	## https://pandas.pydata.org/pandas-docs/stable/indexing.html
	#dfXX.at[numInd+1,'Symbol'] = sn
	# dfZ = pd.DataFrame()
	# dfZ['Symbol'] = sn

	# dfXX = dfXX.append(dfZ)
	# print(dfXX.tail(2))

	## reset the index to 0,1,2..n instead of original index location in company file
	dfXX.reset_index(drop=True, inplace=True)
	#print(dfXX.head(1))

	## creates industry files; 
	## pathI =  \StockHist\industryFiles_NASDAQ
	## filename = the short name.csv
	dfXX.to_csv(os.path.join(pathI, fileName))

### End ###

	



