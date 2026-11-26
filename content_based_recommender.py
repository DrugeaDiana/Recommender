import pandas as pd

# Importing database
metadata = pd.read_csv('../movies_metadata.csv', low_memory=False)

print(metadata['overview'].head())