const unsplashAccessKey = "V8-SX_WOI1p5713vnQDGTPRwUB8V8adNAdJJMxfPGfs"

const formEl = document.querySelector("form")
const inputEl = document.getElementById("search-input")
const searchResults = document.querySelector(".search-results")
const showMore = document.getElementById("show-more-button")

let inputData = ""
let page = 1

async function searchCocktail() {
    inputData = inputEl.value;
    const url = `/cocktail/<${inputData}>`

    console.log(url)
    const response = await fetch(url)
    console.log(response)
    const data = await response.json()
    const results = data.results;
    console.log(results)

    // if (page === 1) {
    //     searchResults.innerHTML = "";
    // }

    // results.map((result) => {
    //     const imageWrapper = document.createElement("div");
    //     imageWrapper.classList.add("search-result");
    //     const image = document.createElement("img");
    //     image.src = result.urls.small;
    //     image.alt = result.alt_description;
    //     const imageLink = document.createElement("a");
    //     imageLink.href = result.links.html;
    //     imageLink.target = "_blank";
    //     imageLink.textContent = result.alt_description;

    //     imageWrapper.appendChild(image);
    //     imageWrapper.appendChild(imageLink);
    //     searchResults.appendChild(imageWrapper);
    // });

    // page++;
    // if (page > 1) {
    //     showMore.style.display = "block";
    // }
}

formEl.addEventListener("submit", (event) => {
    event.preventDefault();
    page = 1;
    searchCocktail();
})

// showMore.addEventListener("click", (event) => {
//     searchImages();
// })