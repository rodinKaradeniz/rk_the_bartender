# When life gives you lemons, you gotta make some lemonade.
# This program contains functionality for suggesting which cocktails can be made
# with the given ingredients.

import pandas as pd
from data_processing.csv_utils import load_ingredient_to_cocktails, refactor_ingredient_name


def available_n_cocktails(ingredients, n=15):
    # Get ingredients_to_cocktails
    ingredients_to_cocktails = load_ingredient_to_cocktails()

    # Score cocktails based on how many of the given ingredients they have
    cocktail_scores = {}
    for ingredient in ingredients:
        refactored_ingredient_name = refactor_ingredient_name(ingredient)
        for cocktail in ingredients_to_cocktails[refactored_ingredient_name]:
            if cocktail in cocktail_scores:
                cocktail_scores[cocktail] += 1
            else:
                cocktail_scores[cocktail] = 1

    # Sort found cocktails according to their scores
    sorted_cocktail_scores = sorted(cocktail_scores.keys(),
                                    key = lambda x: cocktail_scores[x],
                                    reverse=True)
    
    # Return top cocktails with their scores
    top_cocktails = [(i, cocktail_scores[i]) for i in sorted_cocktail_scores]
    return top_cocktails[:n]

    
if __name__ == "__main__":
    ingredients = [
        "kahlua",
        "vodka"
    ]
    recommendations = available_n_cocktails(ingredients, n=10)
    print(recommendations)