/* jshint esversion: 6 */

window.onload = setCurrentAttr;
const navbar = document.getElementById('nav').getElementsByTagName('a');

// Checks current href & sets attribution if href is active
function setCurrentAttr() {
    for(i = 0; i < navbar.length; i++) { 
        if(document.location.href.indexOf(navbar[i].href)>=0) {
            navbar[i].attr('aria-current', 'page');
        }
    }
}