const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const fs = require('fs');

// var Handlebars = require("handlebars");
// var Filter = require("handlebars.filter");
//
// Handlebars.registerHelper("printItems", function(items) {
//   var html = "<ul>";
//   // items.forEach(function(entry) {
//   //   html += "<li>" + entry + "</li>";
//   // });
//   html += "</ul>";
//   return html;
// });
// Filter.registerHelper(Handlebars);



app.use(bodyParser.json());
app.use(express.static("public"));
// app.set('view engine', 'hbs');

// var hbs = require('handlebars');
// hbs.registerHelper("inc", function(value, options)
// {
//     return "asdfasdf" + value;
// });
// app.engine('handlebars', hbs.engine);
var exphbs = require('express-handlebars');
var hbs = exphbs.create({
    helpers: {
        test: function () { return "Lorem ipsum" },
        json: function (value, options) {
            return JSON.stringify(value);
        }
    },
    defaultLayout: 'main',
    partialsDir: ['views/partials/']
});
app.engine('handlebars', hbs.engine);
app.set('view engine', 'handlebars');
app.set('views', path.join(__dirname, 'views'));
/*************/

app.get("/", function(req, res) {
    // res.send("Hello world");
    var data = {
        name: 'damian',
        title: 'hello page'
    }
    res.render('hello.hbs', data);
});

app.get("/hello/:name/age/:age", function(req, res) {
    var data = {
        name: req.params.name,
        age: req.params.age,
        title: 'hello page'
    }
    res.render('hello.hbs', data);
});

app.put("/documents/:filepath", function(req, res) {
    console.log(req.params.filepath);
    var filename = req.params.filepath;
    let filepath = './files/' + filename;
    let contents = req.body.contents;
    fs.writeFile(filepath, contents, function(err) {
        if (err) {
            res.status(500);
            res.json({
                message: 'Couldn\'t save file because: ' + err.message
            });
        } else {
            res.json({
                message: 'File ' + filepath + ' saved.'
            });
        }
    });
});

app.get("/documents/:filepath", function(req, res) {
    var filename = req.params.filepath;
    let filepath = './files/' + filename;
    fs.readFile(filepath, 'utf8', function(err, data) {
        if (err) {
            res.status(500);
            res.json({
                message: 'Couldn\'t save file because: ' + err.message
            });
        } else {
            console.log(data);
            res.json({
                "filepath": "/files/" + filename,
                "contents": data
            });
        }
    });
    console.log(filepath);

});

app.get("/documents/:filepath/display", function(req, res) {
    var filename = req.params.filepath;
    let filepath = './files/' + filename;
    fs.readFile(filepath, 'utf8', function(err, data) {
        if (err) {
            res.status(500);
            res.json({
                message: 'Couldn\'t save file because: ' + err.message
            });
        } else {
            console.log("going to return markup display");
            var contents = {
                "contents": data
            }
            res.render('markup.hbs', contents);
        }
    });
    console.log(filepath);
});

app.get("/documents", function(req, res) {
    fs.readdir("./files", 'utf8', function(err, data) {
        if (err) {
            res.status(500);
            res.json({
                message: 'Couldn\'t read dir file because: ' + err.message
            });
        } else {
            console.log("going to return doc list");
            var contents = {
                "contents": data
            }
            res.json(data);
        }
    });
});

app.delete("/documents/:filepath", function(req, res) {
    var filename = req.params.filepath;
    let filepath = './files/' + filename;
    fs.unlink(filepath, function() {
        res.json({
            "filepath": "/files/" + filename,
            "deleted": true
        });
    });

});

// app.get("/hello/:name",function(req,res){
//     var name = req.params.name || 'world';
//     res.send("Hello " + name);
// });
//
// app.get('/hello', function(req,res){
//     var name = req.query.name || 'world';
//     // console.log(req);
//     res.send("Hello " + name);
// });

app.post('/hello', function(req, res) {
    var name = req.body.name || 'world';
    res.send("Hello " + name);
});

app.listen(3000, function() {
    console.log('running the express app');
});
