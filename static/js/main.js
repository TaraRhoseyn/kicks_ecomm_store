/* jshint esversion: 6 */

const navbar = document.getElementsByTagName('a');

// Checks current href & sets attribution if href is active
// function setCurrentAttr() {
//     console.log("main.js is here");
//     for(i = 0; i < navbar.length; i++) { 
//         if(document.location.href.indexOf(navbar[i].href)>=0) {
//             navbar[i].attr('aria-current', 'page');
//         }
//     };
    
// }
window.onload=function(){
    // Sends user back to previous page
    $("#btn--back").on("click", function() {
        console.log("here");
        history.go(-1);
    });
}
