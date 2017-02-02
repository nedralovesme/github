const express = require('express');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const bodyParser = require('body-parser');

app.use(express.static('public'));
app.use(bodyParser.json());

io.on('connection',function(socket){
    console.log('a user connected');
    socket.on('greeting',function(data){
        console.log('I got this greeting: ',data);
        socket.emit('greeting-reply',{content:'hit you back'});
    });
    socket.on('disconnect',function(){
        console.log('user disconnected');
    });
    socket.broadcast.emit('join','Another user joined');
});
io.emit('welcome','welcome to the demo');

app.get("/hi",function(req,res){
    res.send('hi');
});

http.listen(3000, function(){
    console.log("running on 3000");
});
