# When life gives you lemons, you gotta make some lemonade.

# This program contains functionality for suggesting which cocktails can be made
# with the given ingredients.

import pandas as pd

def available_cocktails(ingredients):
    # Load data
    cocktails = pd.read_csv('db/csv/processed/cocktails.csv')

    # Iteratively lookup for the cocktails that contain the ingredients
    