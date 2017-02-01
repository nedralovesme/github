var async = require('async');
var fs = require('fs');

// function cookTilapia(done){
//     var i = 1000000000*Math.random();
//     console.log(i);
//     while (i>0){
//         i--;
//     }
//     console.log("I cooked tilapia");
//     return done();
// }
// function cookAsparagus(done){
//     var i = 500000000*Math.random();
//     console.log(i);
//     while (i>0){
//         i--;
//     }
//     console.log("I cooked asparagus");
//     return done();
// }
// function makeMeal(done){
//     console.log("I'm about to start cooking");
//     async.parallel([cookTilapia,cookAsparagus],done);
// }
//
// makeMeal(function(){console.log("i'm done cooking!!!")});
try {
    var buffer = fs.readFileSync('helloworldX.js');
    console.log(buffer.toString());
} catch(error){
    console.log("error caught");
}


console.log(process.argv);
