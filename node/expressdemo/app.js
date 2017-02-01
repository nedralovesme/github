// var express = require('express');
// var app = express();
//
// app.get("/",function(req,res){
//     res.send('hello');
// });
//
// app.get('/hello/:name', function(req, res){
//    var name = req.params.name || 'world';
//    res.send("Hello " + name + "!");
// });
//
// app.listen(3000, function(){});

var express = require('express');
var app = express();
// const bodyParser = require('body-parser')

// app.get('/', function(req, res){
//     res.send("Hello world.");
// });

app.get('/hello/:name', function(req, res){
   var name = req.params.name || 'world';
   res.send("Hello " + name + "!");
});

app.post("/login",function(req,res){
    res.send('got a post');
});

app.listen (3000, function(){
   console.log("LAsadeadee!");
});
