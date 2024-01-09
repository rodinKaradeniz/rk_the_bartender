import pandas as pd
import os
import pickle
import re

def update_alcoholic_col(a):
    return a == "Alcoholic"

def refactor_cocktail_df(df: pd.DataFrame) -> pd.DataFrame:
    # Drop last row
    df = df.drop(df.index[-1])

    # Drop unused columns
    df = df[['strDrink', 'strAlcoholic', 'strDrinkThumb', 'strGlass', 'strInstructions'] +
            [f'strIngredient{i}' for i in range(1,16)] +
            [f'strMeasure{i}' for i in range(1,16)]]

    # Remove duplicates
    df = df.drop_duplicates()

    # Change "Alcoholic" col to True/False
    df['strAlcoholic'] = df['strAlcoholic'].apply(update_alcoholic_col)

    # Convert types of columns
    df['strDrink'] = df['strDrink'].astype('string')
    df['strAlcoholic'] = df['strAlcoholic'].astype('bool')
    df['strDrinkThumb'] = df['strDrinkThumb'].astype('string')
    df['strGlass'] = df['strGlass'].astype('string')
    df['strInstructions'] = df['strInstructions'].astype('string')
    for i in range(1, 16):
        df[f"strIngredient{i}"] = df[f"strIngredient{i}"].astype('string')
        df[f"strMeasure{i}"] = df[f"strMeasure{i}"].astype('string')

    # Relabel columns except ingredients and measures
    relabel = {
        'strDrink': 'cocktail_name',
        'strAlcoholic': 'alcoholic',
        'strDrinkThumb': 'image_url',
        'strGlass': 'glass_type',
        'strInstructions': 'recipe'
        }
    for old, new in relabel.items():
        df = df.rename(columns = {old: new})

    # Rename ingredient columns
    for i in range(1, 16):
        df = df.rename(columns = {f"strIngredient{i}": f"ingredient{i}"})

    # Rename measure columns
    for i in range(1, 16):
        df = df.rename(columns = {f"strMeasure{i}": f"measure{i}"})

    # Concatenate ingredients into a new column for content-based recommendation
    ingredient_columns = [f"ingredient{i}" for i in range(1,16)]

    df['ingredients'] = df[ingredient_columns].values.tolist()

    # Remove NaN values from the ingredients column
    df['ingredients'] = df['ingredients'].apply(lambda x: [refactor_ingredient_name(value) for value in x if pd.notna(value)])

    return df


def refactor_ingredient_name(ingredient: str) -> str:
    """
    Helper string manipulation function for removing whitespaces
    and transforming uppercase letters into lowercase letters for the ingredient name.
    """
    refactored_name = ingredient.lower()
    refactored_name = re.sub(r'[^a-z]', '', refactored_name)
    return refactored_name


def load_ingredient_to_cocktails(update=False) -> pd.DataFrame:
    """
    Creates a map from ingredients to cocktails the ingredient is used in.
    Saves the map as a pickle file for future usages, returns the map.
    """
    if os.path.exists("db/csv/processed/ingredient_to_cocktails.pkl") and not update:
        with open('ingredient_to_cocktails.pkl', 'rb') as fp:
            ingredient_to_cocktails = pickle.load(fp)
            return ingredient_to_cocktails
        
    # Load data
    cocktails = pd.read_csv('db/csv/processed/cocktails.csv')

    # key, value = ingredient, [cocktails with that ingredient]
    ingredient_to_cocktails = {}  
    
    for index, row in cocktails.iterrows():
        cocktail = row["cocktail_name"]
        for i in range(1, 16):
            ingredient = row[f"ingredient{i}"]
            if not pd.isna(ingredient):
                refactored_ingredient = refactor_ingredient_name(ingredient)
                if refactored_ingredient in ingredient_to_cocktails:
                    ingredient_to_cocktails[refactored_ingredient].append(cocktail)
                else:
                    ingredient_to_cocktails[refactored_ingredient] = [cocktail]

    # Save ingredient_to_cocktails with pickle
    if update:
        with open('ingredient_to_cocktails.pkl', 'wb') as fp:
            pickle.dump(ingredient_to_cocktails, fp)
    
    return ingredient_to_cocktails


if __name__ == "__main__":
    data = pd.read_csv('db/csv/raw/all_drinks.csv', index_col=0)
    new_data = refactor_cocktail_df(data)
    new_data.to_csv('db/csv/processed/cocktails.csv', index=True)