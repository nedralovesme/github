const express=require("express");
var session = require('express-session');
var uniqid = require('uniqid');
const bcrypt =  require('bcrypt');
const saltRounds = 10;

var app = express();
var sess = {
  secret: 'keyboard cat',
  cookie: { maxAge: 60000 }
}

const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
app.use(bodyParser.json());
// app.use(express.cookieParser());


if (app.get('env') === 'production') {
  app.set('trust proxy', 1) // trust first proxy
  sess.cookie.secure = true // serve secure cookies
}

// use cookie for middleware
app.use(cookieParser('your secret here'));

// Use the session middleware
app.use(session(sess));

//auth function
function auth(req, res, next) {
    console.log("customTHIng:",req.cookies);
  // verify the authentication token
  var sess = req.session;
  if (sess.username) {
    next();
  } else {
    res.status(401);
    res.json({ error: 'You are not logged in lol' });
  }
}

// Access the session as req.session
app.get('/', auth, function (req, res, next) {
  var sess = req.session;
  if (sess.views) {
    sess.views++;
    console.log("session:");
    console.log(sess);
    res.setHeader('Content-Type', 'text/html')
    res.write('<p>views: ' + sess.views + '</p>')
    res.write('<p>expires in: ' + (sess.cookie.maxAge / 1000) + 's</p>')
    res.write('<p>user: ' + sess.username + '</p>')
    res.write('<p>token: ' + sess.token + '</p>')
    res.end()
  } else {
    sess.views = 1
    res.end('welcome to the session demo. refresh!')
  }
});

app.post('/login', function(req, res) {
  var username = req.body.username;
  var password = req.body.password;


  //user = larry, password='open'
  // password='open';
  // bcrypt.genSalt(saltRounds, function(err, salt) {
  //    bcrypt.hash(password, salt, function(err, hash) {
  //    // Store hash in your password DB.
  //    console.log(hash);
  //    //hash = '$2a$10$AwK0fK6ZeppiJikMHyVj4.oHiqysk6cC9uUFdLlAnye3l9qNDaAsC'
  //    });
  //   });
  console.log("password:",password);
  bcrypt.compare(password, '$2a$10$AwK0fK6ZeppiJikMHyVj4.oHiqysk6cC9uUFdLlAnye3l9qNDaAsC', function(err, success) {
      console.log("success",success);
      //res is true|false
      if(success){
          var token=uniqid();
          req.session.username = username;
          req.session.token = token;

          //SET COOKIE TOKEN:
          let options = {
              maxAge: 1000 * 60 * 15, // would expire after 15 minutes
              httpOnly: true, // The cookie only accessible by the web server
              signed: true // Indicates if the cookie should be signed
          }

          // Set cookie
          res.cookie('session', token, options);

          console.log("session is going to be set to:")
          console.log(req.session);
          res.json({
            username: username,
            token: token
          });
      } else {
          res.status(401);
          res.json({
            error: 'Login incorrect'
          });
      }
  });

});

app.get("/logout",function(req,res){
    req.session.destroy();
    res.redirect("/");
});

app.get("/logintest",function(req,res){
    console.log("...............................logintest");
    console.log(req.session);
    console.log(req.cookies);
    if (req.session.token == req.cookies.session){
        res.send("You are logged in");
    } else {
        res.send("You are NOT logged in");
    }
});

app.get('/cookiedemo', function(req,res){
    // read cookies
    console.log(req.cookies)

    let options = {
        maxAge: 1000 * 60 * 15, // would expire after 15 minutes
        httpOnly: true, // The cookie only accessible by the web server
        signed: true // Indicates if the cookie should be signed
    }

    // Set cookie
    res.cookie('customTHIng', 'secret value', options) // options is optional
    res.send("Done with cookie stuff");
});


app.listen(3000,function(){
    console.log("running...");
})
