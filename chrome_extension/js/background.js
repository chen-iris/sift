// background.js is always running while the extnesion is on
// listens to events like key presses or navigating to different pages
chrome.runtime.onInstalled.addListener(function() {
    alert("background.js working");
});