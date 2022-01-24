const searchResult = document.getElementById('search-result-display');

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

function displayNoResult() {
    searchResult.innerHTML = "No";
    var tryAgain = document.getElementById('try-again');
    tryAgain.innerHTML = "Try searching another term.";
    var redirect = document.getElementById('research-btn');
    redirect.innerHTML = `<i class="fas fa-chevron-left"></i>  Keep shopping`;
    tryAgain.classList.add("mb-3");

}

function displayResultNum() {
    var results = document.getElementsByClassName('card-deck');
    var resultsNum = results.length;
    console.log(resultsNum);
    searchResult.innerHTML = resultsNum;

}

window.onload = checkSearchResult();