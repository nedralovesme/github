
//http://passportjs.org/docs/authenticate

const express = require("express");
var session = require('express-session');


function User() {
    var username = "";
    var findone = function(args, done) {
        //grab the username out of the DB
        this.username = args.username;
        console.log("going to login the user");
        done("", this);
    }
    var validPassword = function(password) {
        return true;
    }
    return {
        findone: findone,
        validPassword: validPassword
    }
}

var passport = require('passport'),
    LocalStrategy = require('passport-local').Strategy;

passport.use(new LocalStrategy(
    function(username, password, done) {
        console.log(username, password);
        (User()).findone({
            username: username
        }, function(err, user) {
            console.log("user is");
            console.log(user);
            if (err) {
                return done(err);
            }
            if (!user) {
                return done(null, false, {
                    message: 'Incorrect username.'
                });
            }
            if (!user.validPassword(password)) {
                return done(null, false, {
                    message: 'Incorrect password.'
                });
            }
            console.log("calling the done()");
            return done(null, user);
        });
    }
));

var app = express();
// app.use(require('express-session')({
//   secret: 'keyboard cat',
//   resave: true,
//   saveUninitialized: true
// }));

// Use the session middleware
app.use(session({
    secret: 'keyboard cat',
    cookie: {
        maxAge: 60000
    }
}))

passport.serializeUser(function(user, done) {
    done(null, user);
});

passport.deserializeUser(function(user, done) {
    done(null, user);
});

const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(require('cookie-parser')());
app.use(passport.initialize());
app.use(passport.session());

if (app.get('env') === 'production') {
    app.set('trust proxy', 1) // trust first proxy
    sess.cookie.secure = true // serve secure cookies
}


//auth function
// function auth(req, res, next) {
//     // verify the authentication token
//     var sess = req.session
//     if (req.session.username) {
//         next();
//     } else {
//         res.status(401);
//         res.json({
//             error: 'You are not logged in lol'
//         });
//     }
// }


// Access the session as req.session
app.get('/', passport.authenticate('local'), function (req, res) {
  var sess = req.session;
  if (sess.views) {
    sess.views++
    res.setHeader('Content-Type', 'text/html')
    res.write('<p>views: ' + sess.views + '</p>')
    res.write('<p>expires in: ' + (sess.cookie.maxAge / 1000) + 's</p>')
    res.write('<p>user: ' + sess.user + '</p>')
    res.end()
  } else {
    sess.views = 1
    res.end('welcome to the session demo. refresh!')
  }
});


app.post('/login',
    passport.authenticate('local'),
    function(req, res) {
        // If this function gets called, authentication was successful.
        // `req.user` contains the authenticated user.
        res.redirect('/users/' + req.user.username);
    });

app.get("/logout", function(req, res) {
    req.session.destroy();
    res.redirect("/");
});

app.get("/users/:username", function(req, res) {
    console.log("going to show the user details");
    var username = req.params.username;
    console.log(req.params.username);
    console.log("username:" + username);
    res.status(200);
    res.send('Welcome ' + username);
});

app.listen(3000, function() {
    console.log("running...");
})
