#CS127 Assignment #39: Parking Tickets by David Dekle-Hills

import pandas as pd

csvFile = input('Enter CSV file name: ')
reader = pd.read_csv(csvFile)
print("Top three contributing factors for collisons:")
print(reader["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])

