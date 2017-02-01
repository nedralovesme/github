var async = require('async');
var fs = require('fs');

// function Deck(){
//     this.cards = this.buildDeck();
// }
//
// Deck.prototype.points=[1,2,3,4];
// Deck.prototype.suits=["s","h","d","c"];
//
// Deck.prototype.buildDeck = function(){
//     var cards = [];
//     var deck = this;
//     deck.points.forEach(function(point){
//         //console.log("point is " + point);
//         deck.suits.forEach(function(suit){
//             cards.push([point,suit]);
//         });
//     });
//     return cards;
// }
//
// deck = new Deck();
// console.log(deck.cards);
var name='asdf';
// name=undefined;
function doesNothing(name){
    console.log(name);
}
doesNothing(name);


try {
    var buffer = fs.readFileSync('a-file.txt');
    console.log(buffer.toString());
} catch(error){
    console.log("error caught");
}


console.log(process.argv);
