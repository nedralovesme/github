// var bcrypt = require('bcrypt');
// const saltRounds=10;
// //never store plaintext password!!!!!EVER!!!!EVER!!!!
//
// const myPass = 'secretpw';
// bcrypt.genSalt(saltRounds,function(err,salt){
//     console.log("salt",salt);
//     bcrypt.hash(myPass,salt,function(err, hash){
//         //Will store with user record
//         console.log("hash",hash);
//     });
// });
//
// // hash="$2a$10$FrjwaswIyGTg/RcTvUtpi.xvxSXEQiHHjBqnobQPHMolqDl4N3dGG";
// bcrypt.compare(myPass,hash,function(err,res){
//     console.log("res",res);
// });

const mongoose = require("mongoose");
const bluebird = require("bluebird");

mongoose.Promise = bluebird;
mongoose.connect("mongodb://localhost/proglangs");
const Language = mongoose.model('Language',{
    name:String,
    website:String,
    dateFirstAppeared:Date,
    inventors:[{
        name:String,
        website:String
    }],
    paradigms:[String],
    typingDiscipline:[String],
    newColumn:String
});

// var python = new Language({name:"Python"});
// python.save();
var js = new Language({name:"JavaScript",website:"http://js.org",newColumn:"extra stuff",another:"more data"});
js.save();


// Language.update(
//     {name:'/Python/i'},
//     {$upsert:{website:'http://python.org'}}
// );

// Language.find({name:"Python"}).then(
//     function(docs){
//         console.log("Docs:",docs);
//     }
// )
