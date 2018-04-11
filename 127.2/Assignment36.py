#CS127 Assignment #36: Parking Tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ') #Name of the csv file
attribute = input('Enter attribute:')
tickets = pd.read_csv(csvFile) # Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets["attribute"].value_counts()[:10]) #Print out license plates
