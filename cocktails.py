import requests
import key_config

# def cocktail_api(cocktail_name='bloody mary'):
#     """submit the API query using a variable for the cocktail name and API_KEY"""

#     API_KEY = key_config.KEYS["api_key_ninjas"]

#     API_URL = 'https://api.api-ninjas.com/v1/cocktail?name={}'

#     resp = requests.get(API_URL.format(cocktail_name), headers={'X-Api-Key': API_KEY})

#     if resp.status_code == requests.codes.ok:
#         cocktail_info = resp.json()
#         if len(cocktail_info) == 0:
#             raise Exception(f"Cocktail {cocktail_name} not found. Try a different \
#                             name or check your input for spelling errors.")

#         return cocktail_info[0]
        
#     else:
#         print("Error:", resp.status_code, resp.text)


def get_cocktail(cocktail_name='sex on the beach', key=1):
    """submit the API query with cocktail name and api_key=1 to cocktaildb"""

    API_URL = "http://www.thecocktaildb.com/api/json/v1/{}/search.php?s={}"

    resp = requests.get(API_URL.format(key, cocktail_name))
    if resp.status_code != requests.codes.ok:
        print("Error:", resp.status_code, resp.text)
        return

    results = resp.json()["drinks"]
    if not results:
        raise Exception("Drink not found. Check input for any spelling errors.")
    elif len(results) > 1:
        print(f"Multiple results have been found for \'{cocktail_name}\'")
        print("If this is not the result you are looking for, try to give a more specific input.")
    
    return results[0]


def get_ingredient(ingredient_name='vodka', key=1):
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
    
    return results[0]


def get_random_cocktail(key=1):
    """submit the API query with cocktail name and api_key=1 to cocktaildb"""

    API_URL = "www.thecocktaildb.com/api/json/v1/{}/random.php"

    resp = requests.get(API_URL.format(key))
    if resp.status_code != requests.codes.ok:
        print("Error:", resp.status_code, resp.text)
        return

    results = resp.json()["drinks"]
    
    return results[0]


if __name__ == '__main__':
    get_cocktail()
    get_ingredient()