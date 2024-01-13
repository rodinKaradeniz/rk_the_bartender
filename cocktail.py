class Cocktail:
    def __init__(self):
        self.name = ''
        self.alcoholic = False
        self.image_url = ''
        self.glass_type = ''
        self.ingredients = []
        self.measures = []
        self.recipe = ''

    def populate_cocktail_from_api(self, response):
        self.name = response["strDrink"]
        self.image_url = response["strDrinkThumb"]
        self.glass_type = response["strGlass"]
        self.recipe = response['strInstructions']
        i = 1
        while i < 16 and response[f'strIngredient{i}'] is not None:
            self.ingredients.append(response[f"strIngredient{i}"])
            self.measures.append(response[f"strMeasure{i}"])
            i += 1

    def populate_cocktail_from_db(self, result):
        self.name = result["cocktail_name"]
        self.alcoholic = result["alcoholic"]
        self.image_url = result["image_url"]
        self.glass_type = result["glass_type"]
        self.recipe = result["recipe"]
        self.ingredients = result["ingredients"]
        self.measures = result["measures"]