import pandas as pd

#PART ONE- combine files
import excel files as individual data frames 
salaryData1 = pd.read_excel('\salaryFile1.xlsx')
salaryData2 = pd.read_excel('\salaryFile2.xlsx')
salaryData3 = pd.read_excel('\salaryFile3.xlsx')


# concat all into a single data frame and create csv file
fullSalaryData = pd.concat([salaryData1, salaryData2, salaryData3])
  
# Export data frame into csv
fullSalaryData.to_csv('fullSalaryData.csv', index=False)
  

#PART TWO- search for duplicates
# check for duplicates in any column by entering its name in the designated location in the comment below:
# duplicates = fullSalaryData[fullSalaryData.duplicated(['PLACECOLUMNNAMEHERE'])]

#for this example I picked the Company Name column
duplicates = fullSalaryData[fullSalaryData.duplicated(['Company Name'])]


#view duplicate rows if any, otherwise print "No Duplicates Found!"
if duplicates.empty:
     print("No Duplicates Found!")
else: 
    print(duplicates)
