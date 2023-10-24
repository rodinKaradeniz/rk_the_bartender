# This program makes the necessary API calls and processes the responses.

import requests
import key_config

API_KEY = key_config.KEYS["api_key_dev_cocktaildb"]


def api_get_cocktail(cocktail_name='sex on the beach', key=API_KEY):
    """submit the API query with cocktail name and api_key=1 to cocktaildb"""

    API_URL = "http://www.thecocktaildb.com/api/json/v1/{}/search.php?s={}"

    resp = requests.get(API_URL.format(key, cocktail_name))
    if resp.status_code != requests.codes.ok:
        print("Error:", resp.status_code, resp.text)
        return

    results = resp.json()["drinks"]
    if results == []:
        raise Exception("Drink not found. Check input for any spelling errors.")
    elif len(results) > 1:
        print(f"Multiple results have been found for \'{cocktail_name}\'")
        print("If this is not the result you are looking for, try to give a more specific input.")
    
    result = results[0]

    cocktail = {
        'name': result["strDrink"],
        'image_url': result["strDrinkThumb"],
        'glass': result["strGlass"],
        'ingredients': [],
        'measures': [],
        'recipe': result['strInstructions']
    }

    # Populate the ingredients and measures
    i = 1
    while i < 16 and result[f'strIngredient{i}'] is not None:
        cocktail['ingredients'].append(result[f"strIngredient{i}"])
        cocktail['measures'].append(result[f"strMeasure{i}"])
        i += 1
    
    return cocktail


def api_get_ingredient(ingredient_name='vodka', key=API_KEY):
    """submit the API query with ingredient name and api_key=1 to cocktaildb"""

    API_URL = "http://www.thecocktaildb.com/api/json/v1/{}/search.php?i={}"

    resp = requests.get(API_URL.format(key, ingredient_name))
    if resp.status_code != requests.codes.ok:
        print("Error:", resp.status_code, resp.text)
        return

    results = resp.json()["drinks"]
    if not results:
        raise Exception("Ingredient not found. Check input for any spelling errors.")
    elif len(results) > 1:
        print(f"Multiple results have been found for \'{ingredient_name}\'")
        print("If this is not the result you are looking for, try to give a more specific input.")
    
    result = results[0]

    ingredient = {
        'name': result['strIngredient'],
        'description': result['strDescription']
    }

    return ingredient


def api_get_random_cocktail(key=API_KEY):
    """submit the API query with cocktail name and api_key=1 to cocktaildb"""

    API_URL = "http://www.thecocktaildb.com/api/json/v1/{}/random.php"

    resp = requests.get(API_URL.format(key))
    if resp.status_code != requests.codes.ok:
        print("Error:", resp.status_code, resp.text)
        return

    result = resp.json()["drinks"][0]

    cocktail = {
        'name': result["strDrink"],
        'image_url': result["strDrinkThumb"],
        'glass': result["strGlass"],
        'ingredients': [],
        'measures': [],
        'recipe': result['strInstructions']
    }

    # Populate the ingredients and measures
    i = 1
    while i < 16 and result[f'strIngredient{i}'] is not None:
        cocktail['ingredients'].append(result[f"strIngredient{i}"])
        cocktail['measures'].append(result[f"strMeasure{i}"])
        i += 1
    
    return cocktail


if __name__ == '__main__':
    # print(api_get_cocktail())
    # print(api_get_ingredient())
    print(api_get_random_cocktail())