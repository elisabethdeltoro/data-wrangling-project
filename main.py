import pandas as pd

#PART ONE
# excel files as individual data frames (Special Generals)
sg1 = pd.read_excel('21sg\Central Falls - 11-02-2021.xlsx')
sg2 = pd.read_excel('21sg\Lincoln - 09-07-2021.xlsx')
sg3 = pd.read_excel('21sg\Portsmouth - 11-02-2021.xlsx')
sg4 = pd.read_excel('21sg\Senate 03 - 11-02-2021.xlsx')
sg5 = pd.read_excel('21sg\South Kingstown - 05-04-2021.xlsx')
sg6 = pd.read_excel('21sg\Voters - East Greenwich - 10-05-2021.xlsx')
sg7 = pd.read_excel('21sg\Westerly - 05-04-2021.xlsx')

# concat all into a single data frame (Special Generals)
sg = pd.concat([sg1, sg2, sg3, sg4, sg5, sg6, sg7])
  
# Export data frame into csv (Special Generals)
sg.to_csv('2021_special_generals.csv', index=False)
  
# excel files as individual data frames (Special Primaries)
sp1 = pd.read_excel('21sp\Pawtucket - Ward 06 Primary - 11-02-2021.xlsx')
sp2 = pd.read_excel('21sp\Providence - Ward 15 Primary - 06-08-2021.xlsx')
sp3 = pd.read_excel('21sp\Voters - Senate 03 - 10-05-2021.xlsx')
  
# concat all into a single data frame (Special Primaries)
sp = pd.concat([sp1, sp2, sp3])
  
# Export data frame into csv (Special Primaries)
sp.to_csv('2021_special_primaries.csv', index=False)

#PART TWO
# check for duplicate VOTER IDs (Special Generals)
duplicateRowsSG = sg[sg.duplicated(['VOTER ID'])]

#view duplicate rows if any (Special Generals)
if duplicateRowsSG.empty:
     print("No Duplicates Found in Special Generals!")
else: 
    print(duplicateRowsSG)

    # check for duplicate VOTER IDs (Special Primaries)
duplicateRowsSP = sp[sp.duplicated(['VOTER ID'])]

#view duplicate rows if any (Special Primaries)
if duplicateRowsSP.empty:
     print("No Duplicates Found in Special Primaries!")
else: 
    print(duplicateRowsSP)
