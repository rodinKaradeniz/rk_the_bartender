# When life gives you lemons, you gotta make some lemonade.

# This program contains functionality for suggesting which cocktails can be made
# with the given ingredients.

import pandas as pd
from data_processing.csv_utils import load_ingredient_to_cocktails


def available_cocktails(ingredients):
    # Load data
    cocktails = pd.read_csv('db/csv/processed/cocktails.csv')

    # Get ingredients_to_cocktails
    ingredients_to_cocktails = load_ingredient_to_cocktails(cocktails)

    # Score cocktails based on how many of the given ingredients they have
    cocktail_scores = {}
    for ingredient in ingredients:
        for cocktail in ingredients_to_cocktails[ingredient]:
            if cocktail in cocktail_scores:
                cocktail_scores[cocktail] += 1
            else:
                cocktail_scores[cocktail] = 1

    # Sort found cocktails according to their scores
    sorted_cocktail_scores = sorted(cocktail_scores.keys(),
                                    key = lambda x: cocktail_scores[x],
                                    reverse=True)
    
    # Return top cocktails with their scores
    return [(i, cocktail_scores[i]) for i in sorted_cocktail_scores]

    
if __name__ == "__main__":
    pass