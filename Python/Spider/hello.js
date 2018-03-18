// a phantomjs example
var page = require('webpage').create();
phantom.outputEncoding = "gbk";
page.open("http://www.baidu.com", function (status) {
    if (status === "success") {
        console.log(page.title);
    } else {
        console.log("Page failed to load.");
    }
   
});

// var content = page.evaluate(function () {
//     var element = document.querySelector('#div');
//     return element.textContent;
// });

console.log(content);
phantom.exit()

