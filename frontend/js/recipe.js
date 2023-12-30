const resultContainer = document.getElementById("recipe-result");
const searchBtn = document.getElementById("recipe-search-button");
const searchInput = document.getElementById("recipe-search-input");
const searchContainer = document.querySelector(".recipe-search-box");

// CocktailAPI
const apiUrl = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=";

// Event listeners for search and input (when click search or press "enter")
searchBtn.addEventListener("click", searchCocktail);
searchInput.addEventListener("keydown", function (e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        searchCocktail();
    }
});

fetch("http://127.0.0.1:5000/test").then((response) => response.json()).then((data) => { console.log(data) });

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
                <img
                    id="recipe-img"
                    src=${cocktail.strDrinkThumb}
                    alt=${cocktail.strDrink} />
                <div id="recipe-glass">
                    <h3>Glass:</h3>
                    <h4>${cocktail.strGlass}<h4>
                </div>
                <div id="recipe-ingredients-container">
                    <h3>Ingredients:</h3>
                    <ul>${ingredients}</ul>
                </div>
                <div id="recipe-str">
                    <pre id=recipe-instructions">${cocktail.strInstructions}</pre>
                </div>
                <div id="recipe">
                    <button id="hide-recipe">X</button>
                    <pre id=recipe-instructions">${cocktail.strInstructions}</pre>
                </div>
                    <button id="show-recipe">View Recipe</button>
                </div>
                <div class="recipe-search-box">
                    <input type="text" id="another-cocktail" placeholder="Search Another Cocktail...">
                <button id="another-cocktail-search-button">Search</button>
                </div>
            `;
            resultContainer.innerHTML = recipeHtml;

            const hideRecipeBtn = document.getElementById("hide-recipe");
            hideRecipeBtn.addEventListener("click", hideRecipe);

            const showRecipeBtn = document.getElementById("show-recipe");
            showRecipeBtn.addEventListener("click", showRecipe);

            const nextSearchInput = document.getElementById("another-cocktail");
            nextSearchInput.addEventListener("keydown", function (e) {
                if (e.keyCode === 13) {
                    e.preventDefault();
                    searchCocktail();
                }
            });

            const searchAnotherCocktailBtn = document.getElementById("another-cocktail-search-button");
            searchAnotherCocktailBtn.addEventListener("click", searchCocktail);

            searchContainer.style.opacity = '0';
            searchContainer.style.display = 'none';
        })
        .catch(() => {
            searchContainer.style.opacity = '1';
            searchContainer.style.display = 'grid';
            resultContainer.innerHTML = `<h3>Error fetching data</h3>`;
        });
}

function getIngredients(cocktail) {
    let ingreHtml = "";
    for (let i = 1; i < 21; i++) {
        const ingredient = cocktail[`strIngredient${i}`];
        if (ingredient) {
            const measure = cocktail[`strMeasure${i}`];
            ingreHtml += `<li>${measure} ${ingredient}</li>`;
        } else {
            break;
        }
    }
    return ingreHtml;
}

function hideRecipe() {
    const recipe = document.getElementById("recipe");
    recipe.style.display = "none";
}

function showRecipe() {
    const recipe = document.getElementById("recipe");
    recipe.style.display = "block";
}

function resetContainer() {
    recipeHtml = `
        <div class="recipe-search-box">
            <input type="text" id="recipe-search-input" placeholder="Enter cocktail...">
            <button id="recipe-search-button">Search</button>
        </div>
        <div id="recipe-result"></div>
    `;

    resultContainer.innerHTML += recipeHtml;
}