const express = require('express');

const app = express();

app.get('/hello', function(req, res) {
  var name = req.query.name || 'world';
  res.json({
    message: 'Hello ' + name + '!'
  });
});

app.listen(3000, function() {
  console.log('Example app listening on port 3000!');
});
