import { process } from '/env'


const setupTextarea = document.getElementById('setup-textarea') 
const setupInputContainer = document.getElementById('setup-input-container')
const movieBossText = document.getElementById('movie-boss-text')

const apiKey = process.env.OPENAI_API_KEY
// const apiKey = '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'
const url = 'https://api.openai.com/v1/completions'

document.getElementById("send-btn").addEventListener("click", () => {
  // if (setupTextarea.value) {
    setupInputContainer.innerHTML = `<img src="images/loading.svg" class="loading" id="loading">`
    movieBossText.innerText = `Ok, just wait a second while my digital brain digests that...`
  // }
  fetchBotReply()
})

function fetchBotReply(){
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      'model': 'text-davinci-003',
      'prompt': 'Sound enthusiastic in five words or less.' 
    })
  }).then(response => response.json()).then(data => 
  movieBossText.innerText = data.choices[0].text
  )
}

