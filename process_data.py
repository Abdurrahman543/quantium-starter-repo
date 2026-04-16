import pandas as pd
import os

data_folder = './data'
file_paths = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]

dataframes = []
for file in file_paths:
    df = pd.read_csv(file)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

filtered_df = combined_df[combined_df['product'].str.lower() == 'pink morsel'].copy()

filtered_df['price'] = filtered_df['price'].replace(r'[\$,]', '', regex=True).astype(float)

filtered_df['sales'] = filtered_df['quantity'] * filtered_df['price']

final_df = filtered_df[['sales', 'date', 'region']]

final_df.to_csv('formatted_output.csv', index=False)

print("Data successfully processed and saved to 'formatted_output.csv'")