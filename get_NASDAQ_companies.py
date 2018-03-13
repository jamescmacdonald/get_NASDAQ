## download NASDAQ company lists

import os
import pandas as pd 
import numpy as np 

## urls
NASDAQ = ('http://www.nasdaq.com/screening/companies-by-name.aspx?' + 
'letter=0&exchange=nasdaq&render=download')
NYSE = ('http://www.nasdaq.com/screening/companies-by-name.aspx?' +
'letter=0&exchange=nyse&render=download')
AMEX = ('http://www.nasdaq.com/screening/companies-by-name.aspx?' +
'letter=0&exchange=amex&render=download')
ADR = ('http://www.nasdaq.com/screening/companies-by-industry.aspx?' +
'exchange=NASDAQ&market=ADR&render=download')

## https://pandas.pydata.org/pandas-docs/stable/text.html
## df.str.replace(' ','_')
## df.str.split('-') ## this returns Series of lists - can use str.[] or get()
## df.str.split('_', expand=True) ## this returns a Data Frame with multiple columns
## limit number of splits == df.str.split('_', expand=True, n=1)
## rsplit - work in reverse order of split == str.rsplit('_', expand=True, n=1)

## NASDAQ columns = ('Symbol','Name','LastSale','MarketCap','IPOyear',
## 'Sector','industry','Exchange')

## NASDAQ Company lists from website
dfCompList = pd.DataFrame()
dfNAS = pd.read_csv(NASDAQ, usecols= [0,1,2,3,4,5,6])
dfNAS['Exchange'] = 'NASDAQ' 

## NYSE
## use Symbol as index for the symbol corrections
dfNY = pd.read_csv(NYSE, index_col=0, usecols= [0,1,2,3,4,5,6])
dfNY['Exchange'] = 'NYSE'

#CBS = ['Sector' = 'Consumer Services',	'industry' = 'Television Services']
dfNY.loc['CBS','Sector'] = 'Consumer Services'
dfNY.loc['CBS','industry'] = 'Television Services'

#WP = ['Sector' = 'Miscellaneous', 'industry' = 'Business Services']
dfNY.loc['WP','Sector'] = 'Miscellaneous'
dfNY.loc['WP','industry'] = 'Business Services'
#VALE same as CLF
dfNY.loc['VALE','Sector'] = dfNY.loc['CLF','Sector']
dfNY.loc['VALE','industry'] = dfNY.loc['CLF','industry']
#BF.B = STZ
dfNY.loc['BF.B','LastSale'] = 1000
dfNY.loc['BF.B','MarketCap'] = '1000'
dfNY.loc['BF.B','Sector'] = 'Consumer Non-Durables' #dfNY.loc['STZ','Sector']
dfNY.loc['BF.B','industry'] = dfNY.loc['STZ','industry']
#AKO.B = KO
dfNY.loc['AKO.B','LastSale'] = 1000
dfNY.loc['AKO.B','MarketCap'] = '1000'
dfNY.loc['AKO.B','Sector'] = 'Consumer Non-Durables' #dfNY.loc['KO','Sector']
dfNY.loc['AKO.B','industry'] = dfNY.loc['KO','industry']
#BRK.A & BRK.B = AIG
sym = 'BRK.A'
symCop = 'AIG'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
sym = 'BRK.B'
symCop = 'AIG'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#CRD.A & CRD.B = MMC
sym = 'CRD.A'
symCop = 'MMC'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
sym = 'CRD.B'
symCop = 'MMC'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#HEI.A = HEI
sym = 'HEI.A'
symCop = 'HEI'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#JW.A = NYT
sym = 'JW.A'
symCop = 'NYT'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#LGF.A = DIS
sym = 'LGF.A'
symCop = 'DIS'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#PBR.A = PBR or XOM
sym = 'PBR'
symCop = 'XOM'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#RDS.A & RDS.B = XOM
sym = 'RDS.A'
symCop = 'XOM'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
sym = 'RDS.B'
symCop = 'XOM'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#MOG.A = BA
sym = 'MOG.A'
symCop = 'BA'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']
#TI.A = TI
sym = 'TI.A'
symCop = 'TI'
dfNY.loc[sym,'LastSale'] = 1000
dfNY.loc[sym,'MarketCap'] = '1000'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']

sym = 'PFBC'
symCop = 'USB'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']

sym = 'FRC'
symCop = 'USB'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']

sym = 'TOWN'
symCop = 'USB'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']

sym = 'SE'
symCop = 'CARS'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']

sym = 'GEF'
symCop = 'IP'
dfNY.loc[sym,'Sector'] = dfNY.loc[symCop,'Sector']
dfNY.loc[sym,'industry'] = dfNY.loc[symCop,'industry']

## reset the NYSE df index to 0-n series
dfNY.reset_index(drop=False, inplace=True)
print(dfNY.head(2))

dfAM = pd.read_csv(AMEX, usecols= [0,1,2,3,4,5,6])
dfAM['Exchange'] = 'AMEX'
# rows = dfNAS['Exchange'].shape[0] -- columns use 1

## combine the exchange df's
dfCompList = dfCompList.append(dfNAS,ignore_index=True)
dfCompList = dfCompList.append(dfNY,ignore_index=True)
dfCompList = dfCompList.append(dfAM,ignore_index=True)

## NASDAQ columns = ('Symbol','Name','LastSale','MarketCap','IPOyear',
## 'Sector','industry','Exchange')

dfCompList = dfCompList.drop(columns=['IPOyear'])

## remove whitespace
#dfCompList.index = dfCompList.index.str.strip()  
dfCompList['Symbol'] = dfCompList['Symbol'].str.strip()
dfCompList['Name'] = dfCompList['Name'].str.strip()
#dfCompList['LastSale'] = dfCompList['LastSale'].str.strip()
dfCompList['MarketCap'] = dfCompList['MarketCap'].str.strip()
dfCompList['Sector'] = dfCompList['Sector'].str.strip()
dfCompList['industry'] = dfCompList['industry'].str.strip()

## move or correct industry classifications
## https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas
## change index to 'Symbols' - better for mutilple operations
## https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html
dfCompList = dfCompList.set_index(['Symbol'])

# col_TC = ['Symbols from TC2000','SectorTC','IndustryTC']
# path_TCind = 'new_TC_industry'
# pathI = r'C:\Users\Jim\Documents\StockHist\industryFiles_NASDAQ'

## This is a custom list of symbols that I want to change
## industry classifications for
symChangeFile = 'symToChange_Ind_NASDAQ.csv'
dfX = pd.read_csv(symChangeFile)
## cols = ['symMove','symComp']
for i in range(0, len(dfX) ):
	symM = dfX.loc[i,'symMove']
	symC = dfX.loc[i,'symComp']

	dfCompList.loc[symM,'industry'] = dfCompList.loc[symC,'industry']

## https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.reset_index.html
## reset index back to 0-n series
dfCompList.reset_index(drop=False, inplace=True)
print(dfCompList.head(2))

## Remove characters to save file name in make_IndustryFiles.py
colEdit = ['Sector','industry']
for col in colEdit:
	## this would remove the '-' in Non-Durables
	dfCompList[col] = dfCompList[col].str.replace('-','')
	dfCompList[col] = dfCompList[col].str.replace(' ','-')
	dfCompList[col] = dfCompList[col].str.replace('|','_')
	dfCompList[col] = dfCompList[col].str.replace(':','')
	dfCompList[col] = dfCompList[col].str.replace('/','-')
	dfCompList[col] = dfCompList[col].str.replace('(','')
	dfCompList[col] = dfCompList[col].str.replace(')','')
	dfCompList[col] = dfCompList[col].str.replace(',','')
	dfCompList[col] = dfCompList[col].str.replace('.','')
	dfCompList[col] = dfCompList[col].str.replace(';','')

## add indGroup column
## https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
dfCompList['indGroup'] = dfCompList.Sector.str.cat(dfCompList.industry, sep='_')

## rows = dfCompList.shape  ## rows = df.shape[0] - columns use 1
print('total shape ' + str(dfCompList.shape) )
#print(dfCompList.head(2))

## Remove duplicate Symbols
## http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop_duplicates.html
dfCompList = dfCompList.drop_duplicates(subset='Symbol', keep='last')
## https://stackoverflow.com/questions/44392466/python-drop-duplicated-index-in-pandas-dataframe
## dfCompList = dfCompList[~dfCompList.index.duplicated(keep='last')]
#dfCompList.to_csv('testDUP_NASDAQ_CompanyLists.csv')

print('total shape de-dup ' + str(dfCompList.shape) )
#print(dfCompList.head(2))

symRemove_File = open('sym_toRemove.txt', 'r')
symRemove_List = symRemove_File.read().splitlines()
print('dfRem len = ' + str(len(symRemove_List)) )

dfCompList = dfCompList[~dfCompList['Symbol'].isin(symRemove_List)]
print('new total shape ' + str(dfCompList.shape) )
#dfCompList.to_csv('testDF_NASDAQ_CompanyLists.csv')

## Remove symbols that contain '\^' from the index
dfCompList['badSym'] = dfCompList['Symbol'].str.contains('\^', na=False) ## remove '^'
# dfCompList['badSym2'] = dfCompList['Symbol'].isin(['^'])
dfCompList = dfCompList[dfCompList['badSym'] == False]
dfCompList = dfCompList.drop(columns=['badSym'])
print('shape after\^ = ' + str(dfCompList.shape))

#dfCompList['2dots'] = dfCompList['Symbol'].str.count('\.')

## Remove rows with null LastSale
dfCompList = dfCompList[dfCompList['LastSale'].notnull()]
print('shape after LastSale.notnull = ' + str(dfCompList.shape))
dfCompList.to_csv('preNameFilters_NASDAQ_CompanyLists.csv')

## Remove ETFs
dfCompList['ETN'] = dfCompList['Name'].str.contains(' ETN', na=False) ## remove ETN's
dfCompList = dfCompList[dfCompList['ETN'] == False]
dfCompList = dfCompList.drop(columns=['ETN'])
print('shape after ETN = ' + str(dfCompList.shape))
## Remove ETNs
dfCompList['ETF'] = dfCompList['Name'].str.contains(' ETF', na=False) ## remove ETN's
dfCompList = dfCompList[dfCompList['ETF'] == False]
dfCompList = dfCompList.drop(columns=['ETF'])
print('shape after ETF = ' + str(dfCompList.shape))
## remove 'Acquisition Corps'
dfCompList['Acqu'] = dfCompList['Name'].str.contains(' Acquisition', na=False)
dfCompList = dfCompList[dfCompList['Acqu'] == False]
dfCompList = dfCompList.drop(columns=['Acqu'])
print('shape after Acqu = ' + str(dfCompList.shape))
## remove 'Funds'
dfCompList['Fund'] = dfCompList['Name'].str.contains(' Fund', na=False)
dfCompList = dfCompList[dfCompList['Fund'] == False]
dfCompList = dfCompList.drop(columns=['Fund'])
print('shape after Fund = ' + str(dfCompList.shape))

dfCompList.to_csv('preCapSectorFilter_NASDAQ_CompanyLists.csv')

dfCompList = dfCompList[dfCompList['MarketCap'].notnull()]
print('shape after MarketCap null = ' + str(dfCompList.shape))

dfCompList = dfCompList[dfCompList['Sector'].notnull()]  ## remove rows with n/a Sectors
print('shape after Sector null = ' + str(dfCompList.shape))

dfCompList = dfCompList[dfCompList['LastSale'] >= 1] ## remove names with price under $1.00
print('shape after LastSale\>1 = ' + str(dfCompList.shape))


# ## https://pandas.pydata.org/pandas-docs/stable/cookbook.html
# dfCompList.loc[dfCompList.M == True, 'MCapScale'] = 'M'; dfCompList
# dfCompList.loc[dfCompList.B == True, 'MCapScale'] = 'B'; dfCompList

# x = np.array(dfCompList['MCapValue'])
# x.astype(float)
# dfCompList['MCapValue'] = x

print('final total shape = ' + str(dfCompList.shape) )

## sort by Symbol A to Z
dfCompList.sort_values(by=['Symbol'], inplace=True, na_position='first')

## reset index to 0,1,..n series
dfCompList.reset_index(drop=True, inplace=True)

dfCompList.to_csv('NASDAQ_CompanyLists.csv')

## Create Symbol list in separate csv
#col = ['Symbols','Name','Sector','industry','Exchange','indGroup']
dfCompList['Symbol'].to_csv('NASDAQ_symbols.csv', header='Symbol')

## Create list of unique indGroups
NASDAQ_indGroups = pd.DataFrame(data=dfCompList['indGroup'], columns=['indGroup'])
## get unique indGroups
NASDAQ_indGroups = NASDAQ_indGroups.drop_duplicates(subset='indGroup', keep='last')
## sort A-X
NASDAQ_indGroups.sort_values(by=['indGroup'], inplace=True, na_position='first')
## reset index to 0-n
NASDAQ_indGroups.reset_index(drop=True, inplace=True)

## NASDAQ_indGroups['indCount'] = 
NASDAQ_indGroups.to_csv('NASDAQ_indGroups.csv')

#print(dfCompList.at('AJX'))

#quoteFile = 'out_NASDAQ_getQuote.csv'
#quoteCol = ('sharesOutstanding','dividendYieldAnnual','twelveMnthPct','marketCap')
