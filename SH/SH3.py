import pandas as pd
import re

# Load the .csv file into a Pandas DataFrame
df = pd.read_csv('file.csv', sep=',', index_col=False, dtype='unicode', low_memory=False, on_bad_lines='skip')
#df = pd.read_csv('Book1.csv')

# Create a list to store the blended data
blended_data = []

output = input("\nName your file => ") # Ask the user for desired filename
print("\nReading files, please wait...\n")

# Loop through each row in the original DataFrame
for i, row in df.iterrows():
  first_name = re.sub('[^A-Za-z0-9]+', '', str(row['FIRSTNAME']))
  last_name = re.sub('[^A-Za-z0-9]+', '', str(row['LASTNAME']))
  address1 = row['ADDRESS1']
  city = row['CITY']
  state = row['STATE']
  zip = row['ZIP']

  # Loop through each email/phone combination
  for j in range(7, 37):
    email = row['EMAIL' + str(j - 6)]
    if email == '':
      continue

    for k in range(37, 67):
      phone = row['PHONE' + str(k - 36)]
      if phone == '':
        continue

      blended_data.append([first_name, last_name, address1, city, state, zip, email, phone])

# Convert the list of blended data into a new DataFrame
blended_df = pd.DataFrame(blended_data, columns=['FIRSTNAME', 'LASTNAME', 'ADDRESS1', 'CITY', 'STATE', 'ZIP', 'EMAIL', 'PHONE'])

# Remove duplicates from the blended DataFrame
blended_df = blended_df.drop_duplicates()

# Save the blended DataFrame to a .csv file
blended_df.to_csv(output + ".csv", sep=',', encoding='utf-8', index=False)

print(f'Results have been succesfully saved on file: {output}.csv \nDone ✅')
