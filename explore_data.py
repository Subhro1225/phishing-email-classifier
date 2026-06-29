import pandas as pd
import os

# loading all csv files
data_folder = "data/"
all_file = os.listdir(data_folder)

# print(df.shape) // prints the number of rows present in the dataframe

# loading and combining all files
all_datasets = []

for file in all_file:
    file_path = data_folder + file
    df = pd.read_csv(file_path)
    all_datasets.append(df)

# Combine into one big dataframe
combined_df = pd.concat(all_datasets, ignore_index= True)

# droping unwanted columns
combined_df = combined_df.drop(columns=['receiver','date','urls','sender'])

# droping the rows with null & duplicate values
combined_df = combined_df.dropna() # .dropna() "drops rows with na not available"

# print(combined_df.isnull().sum())  // counts and prints sum of all the null rows
# print(combined_df.duplicated().sum()) // cpunts total number of duplicate values

# print(combined_df['label'].value_counts()) // counts the different value of the row.

combined_df.to_csv(data_folder + "clean_data.csv", index=False) 



