"""
File:           Assignment1_digital_forensics_group2.py
Author:         Group 2 - Aukje Hekstra
Date:           11-10-2023
Description:    A script that shows the 
                data analisis of the list of darkweb market products
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Import the excel sheet
excel_sheet_data = pd.read_excel("Assignment 1.xlsx")





# Find the different catagories
print("The different catagories are:")
# get the unique catagories that are in the data
unique_catagories = excel_sheet_data.groupby('Category').first()
# category is now index of dataframe, so turn back into column
unique_catagories.reset_index(inplace=True)
print(unique_catagories['Category'], "\n\n")



# Find the top 10 sellers
# 1. top 10 sellers of most sold products
# 2. top 10 of star rating

# Top 10 sellers of most sold products
print("Top 10 sellers who sold the most successful transactions")
# get rows of first time each unique seller occurs
unique_sellers = excel_sheet_data.groupby('Seller').first()
# seller name is now index of dataframe, so turn back into column
unique_sellers.reset_index(inplace=True)

# sort by successful number of transactions
transactions_sorted = unique_sellers.sort_values('Successful number of transactions',ascending=False)
# make dataframe index correspond with position in dataframe
transactions_sorted.reset_index(inplace=True)

# get top 10 values
top10 = transactions_sorted[['Seller', 'Successful number of transactions','Name']].iloc[:10]
# show in console and output it as a file
top10.to_excel('seller_transactions_top_10.xlsx')
print(top10,"\n\n")



# Top 10 sellers of star rating
print("Top 10 sellers who have the highest rating")

# sort by rating of a seller
star_rating_sorted = unique_sellers.sort_values('Seller rating (%)',ascending=False)
# make dataframe index correspond with position in dataframe
star_rating_sorted.reset_index(inplace=True)

# get top 10 values
top10 = star_rating_sorted[['Seller', 'Seller rating (%)']].iloc[:10]
# show in console and output it as a file
top10.to_excel('seller_rating_top_10.xlsx')
print(top10,"\n\n")



# Get plot of prices per category
excel_sheet_data.boxplot(by = 'Category', column = ['Price'], rot = 60, grid = False, sym = "")  
plt.title('Price in $ per category')
plt.suptitle('')
plt.xlabel('')
plt.show()





