const searchResult = document.getElementById('search-result-display');

// Checks search results page to see whether there were any results
function checkSearchResult() {
    var url = window.location.href;
    if (url.includes("search")) {
        if (document.getElementById('search-result')) {
            displayResultNum();
        } else {
            displayNoResult();
        }
    } else {
        return
    }
}

// Gives feedback that no search results were found, directs to products.html
function displayNoResult() {
    searchResult.innerHTML = "No";
    var tryAgain = document.getElementById('try-again');
    tryAgain.innerHTML = "Try searching another term.";
    var redirect = document.getElementById('research-btn');
    redirect.innerHTML = `<i class="fas fa-chevron-left"></i>  Keep shopping`;
    tryAgain.classList.add("mb-3");

}

// Gives feedback of how many search results were found
function displayResultNum() {
    var results = document.getElementsByClassName('card-deck');
    var resultsNum = results.length;
    console.log(resultsNum);
    searchResult.innerHTML = resultsNum;

}

// Inits check on search results
window.onload = checkSearchResult();