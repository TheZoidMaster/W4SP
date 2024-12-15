console.log("%cactively running on php 🐘", "color: #fd0; font-size: 32pt; font-weight: 800; font-family: monospace;")

let tabs = document.getElementsByClassName("tab");

function iterrHtml(htmlCollection, iterrateFunc) {
    for (let i=0; i<htmlCollection.length; i++) {
        iterrateFunc(htmlCollection[i]);
    }
};

iterrHtml(tabs, function (element) {
    element.addEventListener("click", function() {
        iterrHtml(tabs, function (element) {
            element.className = "tab";
        });
        element.className = "tab active";
    });
});