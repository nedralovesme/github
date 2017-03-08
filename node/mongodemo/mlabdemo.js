//go to https://mlab.com/home
//signup and create a user/database
//add a user to your database
const mongoose = require("mongoose");
const bluebird = require("bluebird");


//IMPORTANT:
//the user/pass is not the mLab username password
//user/pass is a db user you need to create for your collection
//here: https://mlab.com/home
var uri = 'mongodb://<username>:<password>@ds021691.mlab.com:21691/<collectionname>';
db = mongoose.connect(uri);

mongoose.Promise = bluebird;
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

var js = new Language({name:"JavaScript",website:"http://js.org",newColumn:"extra stuff",another:"more data"});
js.save();
