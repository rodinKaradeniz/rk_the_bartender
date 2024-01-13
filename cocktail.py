class Cocktail:
    def __init__(self):
        self.name = ''
        self.image_url = ''
        self.glass = ''
        self.ingredients = []
        self.measures = []
        self.recipe = ''

    def populate_cocktail_from_api(self, response):
        self.name = response["strDrink"]
        self.image_url = response["strDrinkThumb"]
        self.glass = response["strGlass"]
        self.recipe = response['strInstructions']
        i = 1
        while i < 16 and response[f'strIngredient{i}'] is not None:
            self.ingredients.append(response[f"strIngredient{i}"])
            self.measures.append(response[f"strMeasure{i}"])
            i += 1