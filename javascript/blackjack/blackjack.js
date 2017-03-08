function Card(point, suit) {

    var getImageUrl = function() {
        var cardValue = "";
        switch (point) {
            case 1:
                cardValue = "ace";
                break;
            case 11:
                cardValue = "jack";
                break;
            case 12:
                cardValue = "queen";
                break;
            case 13:
                cardValue = "king";
                break;
            default:
                cardValue = point;
        }
        return "images/" + cardValue + "_of_" + suit + ".png";
    }

    var getValue = function() {
        if (point > 10) {
            return 10;
        } else if (isAce()) {
            return 11;
        } else {
            return point;
        }
    }

    var isAce = function() {
        return point == 1;
    }

    return {
        "getImageUrl": getImageUrl,
        "getValue": getValue,
        "isAce": isAce
    };
}

function Deck() {
    var cards = [];
    var suits = ["spades", "hearts", "clubs", "diamonds"];
    for (i = 1; i <= 13; i++) {
        for (s = 0; s < 4; s++) {
            card = Card(i, suits[s]);
            cards.push(card);
        }
    }
    var shuffle = function() {
        var currentIndex = cards.length,
            temporaryValue, randomIndex;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

            // Pick a remaining element...
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex -= 1;

            // And swap it with the current element.
            temporaryValue = cards[currentIndex];
            cards[currentIndex] = cards[randomIndex];
            cards[randomIndex] = temporaryValue;
        }
    }
    shuffle();
    var getCard = function() {
        return cards.pop();
    }
    return {
        getCard: getCard
    }
}

function Hand(player) {
    var cards = [];
    var numAces = 0;
    var addCard = function(card) {
        if (card.isAce()) {
            numAces++;
        }
        console.log("I am adding a card to the hand: " + card.getImageUrl());
        cards.push(card);
        $("#" + player + "-hand").append("<img src='" + card.getImageUrl() + "' />");
        $("#" + player + "-points").text(getScore());
    }
    var getScore = function() {
        var score = 0;
        for (var i = 0; i < cards.length; i++) {
            var card = cards[i];
            score += card.getValue();
        }
        //if I'm over 21 and i have aces:
        aceIndex = 1;
        while (aceIndex <= numAces) {
            if (score > 21) {
                score = score - 10;
            }
            aceIndex++;
        }
        return score;
    }
    return {
        "addCard": addCard,
        "getScore": getScore
    };
}

function Game() {
    var deck = Deck();
    var dealerHand = Hand("dealer");
    var playerHand = Hand("player");
    var message = "";
    $("#dealer-hand").empty();
    $("#player-hand").empty();
    $("#dealer-points").text("");
    $("#player-points").text("");
    $("#messages").text("");
    var deal = function() {
        $("#deal-button").prop("disabled", true);
        $("#hit-button").prop("disabled", false);
        $("#stand-button").prop("disabled", false);
        playerHand.addCard(deck.getCard());
        dealerHand.addCard(deck.getCard());
        playerHand.addCard(deck.getCard());
        if (playerHand.getScore() == 21) {
            message = "Player Wins!";
            endGame();
        }
        dealerHand.addCard(deck.getCard());
        if (dealerHand.getScore() == 21) {
            message = "Dealer Wins!";
            endGame();
        }
    }
    var playerHit = function() {
        playerHand.addCard(deck.getCard());
        if (playerHand.getScore() > 21) {
            message = "Player Busts!";
            endGame();
        }
    }
    var playerStand = function() {
        $("#hit-button").prop("disabled", true);
        $("#stand-button").prop("disabled", true);
        while (dealerHand.getScore() <= 16) {
            dealerHand.addCard(deck.getCard());
        }
        if (dealerHand.getScore() > 21) {
            message = "Dealer busts";
        } else if (dealerHand.getScore() > playerHand.getScore()) {
            message = "Dealer wins";
        } else if (dealerHand.getScore() == playerHand.getScore()) {
            message = "Push";
        } else {
            message = "Player wins!"
        }
        endGame();
    }
    var endGame = function() {
        $("#messages").append("<h1>" + message + "</h1>");
        $("#hit-button").prop("disabled", true);
        $("#stand-button").prop("disabled", true);
        $("#deal-button").prop("disabled", false);
    }
    return {
        deal: deal,
        playerHit: playerHit,
        playerStand: playerStand
    };
}

$(document).ready(function() {
    var game;
    $("#hit-button").prop("disabled", true);
    $("#stand-button").prop("disabled", true);
    $("#deal-button").click(function() {
        game = Game();
        game.deal();
    });
    $("#hit-button").click(function() {
        game.playerHit();
    });
    $("#stand-button").click(function() {
        game.playerStand();
    });
});
