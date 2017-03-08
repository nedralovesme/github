const express=require("express");
var session = require('express-session');
var uniqid = require('uniqid');

var app = express();
var sess = {
  secret: 'keyboard cat',
  cookie: {}
}

const bodyParser = require('body-parser');
app.use(bodyParser.json());

if (app.get('env') === 'production') {
  app.set('trust proxy', 1) // trust first proxy
  sess.cookie.secure = true // serve secure cookies
}

// Use the session middleware
app.use(session({ secret: 'keyboard cat', cookie: { maxAge: 60000 } }))


//auth function
function auth(req, res, next) {
  // verify the authentication token
  var sess = req.session
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
  // verify the login
  if (username === 'larry' && password === 'open') {
    // return the auth token, normally you would
    // generate a random one here, but we are
    // using a hardcoded token, see above
    var token=uniqid();
    req.session.username = username;
    req.session.token = token;
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

app.get("/logout",function(req,res){
    req.session.destroy();
    res.redirect("/");
});
app.listen(3000,function(){
    console.log("running...");
})
