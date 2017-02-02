var socket = io();
socket.emit('greeting','Hello');
socket.on('greeting-reply',function(data){console.log("got some data back from the server:");
console.log(data);});
socket.on('join',function(data){
    console.log("user joined:");
    console.log(data);
});
socket.on('welcome',function(data){
    console.log("user welcome:");
    console.log(data);
});
