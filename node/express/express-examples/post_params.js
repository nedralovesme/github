const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

app.post('/hello', function(req, res) {
  var name = req.body.name || 'world';
  res.send('Hello ' + name + '!');
});

app.listen(3000, function() {
  console.log('Example app listening on port 3000!');
});
