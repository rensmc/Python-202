import pandas as pd
import re

# Load the .csv file into a pandas DataFrame
df = pd.read_csv('file.csv')

# Create an empty DataFrame to store the blended data
blended_df = pd.DataFrame(columns=['FIRSTNAME', 'LASTNAME', 'ADDRESS1', 'CITY', 'STATE', 'ZIP', 'EMAIL', 'PHONE'])

# Loop through each row in the original DataFrame
for index, row in df.iterrows():
    # Loop through each email in the row
    for email in row.iloc[6:36]:
        if not pd.isnull(email):
            # Loop through each phone in the row
            for phone in row.iloc[36:66]:
                if not pd.isnull(phone):
                    # Remove special characters from FIRSTNAME and LASTNAME
                    first_name = re.sub(r'[^\w\s]', '', row['FIRSTNAME'])
                    last_name = re.sub(r'[^\w\s]', '', row['LASTNAME'])
                    
                    # Add a new row to the blended DataFrame with the current email and phone
                    blended_df = blended_df.append({
                        'FIRSTNAME': first_name,
                        'LASTNAME': last_name,
                        'ADDRESS1': row['ADDRESS1'],
                        'CITY': row['CITY'],
                        'STATE': row['STATE'],
                        'ZIP': row['ZIP'],
                        'EMAIL': email,
                        'PHONE': phone
                    }, ignore_index=True)

# Remove duplicates from blended DataFrame
blended_df.drop_duplicates(subset=None, keep='first', inplace=True)

# Save the blended DataFrame to a new .csv file
blended_df.to_csv('blended_data3.csv', index=False)