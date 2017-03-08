var express = require('express');
var app = express();
var morgan = require('morgan');
var logger = morgan('combined');
// var passport = morgan('passport');
var fs = require('fs');
var bodyParser = require('body-parser');
var uniqid = require('uniqid');

/***************/
var cookieParser = require('cookie-parser');
var cookieSession = require('cookie-session');
var session = require('express-session');


var token = 'Keep me a secret';

app.use(bodyParser.json());



// set a cookie
// app.use(cookieParser());

// app.use(function (req, res, next) {
//   // check if client sent cookie
//   var cookie = req.cookies.cookieName;
//   if (cookie === undefined)
//   {
//     // no: set a new cookie
//     var randomNumber=Math.random().toString();
//     randomNumber=randomNumber.substring(2,randomNumber.length);
//     res.cookie('cookieName',randomNumber, { maxAge: 900000, httpOnly: true });
//     console.log('cookie created successfully');
//   }
//   else
//   {
//     // yes, cookie was already present
//     console.log("cookie token",req.cookies);
//     console.log('cookie exists', cookie);
//   }
//   next(); // <-- important!
// });

// app.use(cookieParser('config.cookieSecret'))
// app.use(cookieSession({
//   secret: 'secret-key-you-don\'t-tell-the-client',
//   signed: true
// }));

// app.use(cookieSession({
//   name: 'session',
//   secret: 'secret-key-||||you-don\'t-tell-the-client',
//   keys: ['key1', 'key2']
// }))

// var passport = require('passport')
//   , LocalStrategy = require('passport-local').Strategy;
//
// passport.use(new LocalStrategy(
//   function(username, password, done) {
//       console.log('trying passport local');
//     User.findOne({ username: username }, function (err, user) {
//       if (err) { return done(err); }
//       if (!user) {
//         return done(null, false, { message: 'Incorrect username.' });
//       }
//       if (!user.validPassword(password)) {
//         return done(null, false, { message: 'Incorrect password.' });
//       }
//       return done(null, user);
//     });
//   }
// ));

app.use(session({secret: 'keyboard cat'}));

function auth(req, res, next) {
  // verify the authentication token
  // console.log(req.cookies.session);
  console.log("session in auth:",req.session.token);
  var sessionToken = req.session.token || "";
  if (sessionToken === token) {
    next()
  } else {
    res.status(401);
    res.json({ error: 'You are not logged in lol' });
  }
}

// app.use(passport.initialize());
// app.use(passport.session());

/***************/

// function do1(req,res,next){
//     console.log("do 1");
//     next();
// }
// function do2(req,res,next){
//     console.log("do 2");
//     next();
// }

app.use(function(req,res,next){
    console.log(req.method, req.path);
    next();
});

// setup the logger
// create a write stream (in append mode)
var accessLogStream = fs.createWriteStream(__dirname + '/access.log', {flags: 'a'});

app.use(morgan('combined', {stream: accessLogStream}))


// app.use(do2);

app.get('/',auth,function(req,res){
    req.session.name = 'session name is here';
    //delete req.session.name
    // delete req.session;
    res.send('got it:' , token);
});

app.get('/session',function(req,res){
    // req.session.name = 'Napoleon';
    var session = req.session.name || 'no session';
    res.send('session',session);
});

app.get('/api/data', auth, function(req, res) {
      var theData = [
        { name: 'blah' },
        { name: 'more blah' },
      ];
      console.log("cookies:");
      console.log(req.cookies);
      res.json(theData);
    });

app.post('/login',
  // passport.authenticate('local'),
  function(req, res) {
      console.log(req.body);
      var username = req.body.username;
      var password = req.body.password;
      console.log(username,password);
      // verify the login
      token=uniqid();
      console.log("token:",token);
    //   res.cookie('token',token);
      if (username === 'larry' && password === 'open') {
          //res.cookies('token', token);
        //   res.cookie('token', token);
        //   res.cookie('cookieName',token, { maxAge: 900000, httpOnly: true });
        // req.session.token = token;
        // console.log("cookie from login:");
        // console.log(req.cookies);
        // return the auth token, normally you would
        // generate a random one here, but we are
        // using a hardcoded token, see above
        req.session.token = token;
        console.log("session: ",req.session.token);
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

app.listen(3000,function(){

});
