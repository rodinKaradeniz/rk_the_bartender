import requests
import key_config

# This is not a real API key
API_KEY = key_config.KEYS["api_key_ninjas"]

API_URL = 'https://api.api-ninjas.com/v1/cocktail?name={}'

def cocktail_api(cocktail_name='bloody mary'):
    """submit the API query using a variable for the cocktail name and API_KEY"""
    resp = requests.get(API_URL.format(cocktail_name), headers={'X-Api-Key': API_KEY})
    if resp.status_code == requests.codes.ok:
        cocktail_info = resp.json()
        if len(cocktail_info) == 0:
            raise Exception(f"Cocktail {cocktail_name} not found. Try a different \
                            name or check your input for spelling errors.")

        return cocktail_info[0]
        
    else:
        print("Error:", resp.status_code, resp.text)

if __name__ == '__main__':
    print(cocktail_api("bloody mary"))