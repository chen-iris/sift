/*
// split URL into different parts
var pathArray = window.location.pathname.split('/');
// get site name (Ex. ca.zaful.com)
var siteName = pathArray[1];
*/

chrome.tabs.query({'active': true}, function (tabs) {
    var url = tabs[0].url;
});

function findCurrentSite(siteName) {
    choices = ['Zaful', 'Shein', 'Amazon']
    switch(siteName) {
        case "ca.zaful.com":
            return choices[0];
        case "ca.shein.com":
            return choices[1];
        case "www.amazon.ca":
            return choices[2];
        default:
            return "invalid";
    }
}

/*
console.log(siteName);
console.log(findCurrentSite(siteName));
*/