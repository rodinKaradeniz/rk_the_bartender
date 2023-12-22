const resultContainer = document.getElementById("recipe-result");
const searchBtn = document.getElementById("recipe-search-button");
const searchInput = document.getElementById("recipe-search-input");
const searchContainer = document.querySelector(".recipe-search-box");

// CocktailAPI
const apiUrl = "www.thecocktaildb.com/api/json/v1/1/search.php?s=";

// Event listeners for search and input (when click search or press "enter")
searchBtn.addEventListener("click", searchCocktail);
searchInput.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        searchCocktail();
    }
});

// handle cocktail search
function searchCocktail() {
    const userInput = searchInput.value.trim();
    if (!userInput) {
        resultContainer.innerHTML = `<h3>Input Field Cannot Be Empty</h3>`;
        return;
    }

    fetch(apiUrl + userInput)
        .then((response) => response.json())
        .then((data) => {
            const cocktail = data.drinks[0];
            if (!cocktail) {
                resultContainer.innerHTML = `<h3>No Cocktail Found, Please Try Again!</h3>`;
                return;
            }

            const ingredients = getIngredients(cocktail);
            const recipeHtml = `
                <div class="recipe-details">
                    <h2>${cocktail.strDrink}</h2>
                </div>
                <img src=${cocktail.strDrinkThumb} alt=${cocktail.strDrink} />
                <div id="recipe-glass">
                    <h3>Glass:${cocktail.strGlass}</h3>
                </div>
                <div id="recipe-ingredients-container">
                    <h3>Ingredients:</h3>
                    <ul>${ingredients}</ul>
                </div>
                <div id="recipe">
                    <button id="hide-recipe">X</button>
                    <pre id=instructions">${cocktail.strInstructions}</pre>
                </div>
                <button id="show-recipe">View Recipe</button>
            `;
            resultContainer.innerHTML = recipeHtml;

            const hideRecipeBtn = document.getElementById("hide-recipe");
            hideRecipeBtn.addEventListener("click", hideRecipe);

            const showRecipeBtn = document.getElementById("show-recipe");
            showRecipeBtn.addEventListener("click", showRecipe);

            searchContainer.style.opacity = '0';
            searchContainer.style.display = 'none';
        })
        .catch(() => {
            searchContainer.style.opacity = '1';
            searchContainer.style.display = 'grid';
            resultContainer.innerHTML = `<h3>Error fetching data</h3>`;
        });
}

function getIngredients() {
    pass
}

function hideRecipe() {
    pass
}

function showRecipe() {
    pass
}