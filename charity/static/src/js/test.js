odoo.define('charity.test', function(){
    "use strict";
      // API for get requests
        let fetchRes = fetch(
        "https://lms.saneemnurseries.com/course");
        // fetchRes is the promise to resolve
        // it by using.then() method
        fetchRes.then(res =>
            res.json()).then(d => {
                console.log("d is here", d)
                d.title= name;
                alert("show time")
                prompt("enter your age")
            })
    console.log("javascript is working ");


});