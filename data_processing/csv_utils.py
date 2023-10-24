import pandas as pd


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

    return df


def load_cocktails_to_ingredients(df: pd.DataFrame) -> pd.DataFrame:
    pass


def load_ingredients_to_cocktails(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: think about a way to make this more efficient.

    # key, value = ingredient, [cocktails with that ingredient]
    ingredients_to_cocktails = {}  
    
    for index, row in df.iterrows():
        cocktail = row["cocktail_name"]
        for i in range(1, 16):
            ingredient = row[f"ingredient{i}"]
            if ingredient in ingredients_to_cocktails:
                ingredients_to_cocktails[ingredient].append(cocktail)
            else:
                ingredients_to_cocktails[ingredient] = [cocktail]

    # TODO: Save this as csv also, then add an if condition to the beginning
    # that checks os.exists() for that csv
    return ingredients_to_cocktails


if __name__ == "__main__":
    data = pd.read_csv('db/raw/all_drinks.csv', index_col=0)
    new_data = refactor_cocktail_df(data)
    new_data.to_csv('db/processed/cocktails.csv', index=True)