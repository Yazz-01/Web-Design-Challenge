# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
from scipy.stats import sem
import numpy as np
import csv
import dataframe_image as dfi

# Study data files
cities_path = "Resources/cities.csv"

# Read the cities data 
cities_data = pd.read_csv(cities_path)

# Combine the data into a single dataset
cities_df= pd.DataFrame(cities_data)
# Display the data table for preview
print(cities_df.to_html())
#print(cities_df)

