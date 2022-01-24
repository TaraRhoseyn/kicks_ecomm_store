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
    
}

function displayResultNum() {
    var results = document.getElementsByClassName('card-deck');
    var resultsNum = results.length;
    console.log(resultsNum);
    searchResult.innerHTML = resultsNum;

}

window.onload = checkSearchResult();