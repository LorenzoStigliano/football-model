# Football model.

# Using machine learning techniques to predict outcomes of football matches
# using historical data.

# Classification task in order to predict correct outcome (Win, Loss or Draw)
# Feature vector will have all the stats we want and then we tag it appropriately
# tag the vector with W, L OR D

# Importing the data.
import csv

with open('E0.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Date'], row['Time'])
