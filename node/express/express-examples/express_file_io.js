const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
app.use(bodyParser.json());

app.post('/save_file', function(req, res) {
  let filepath = './files/' + req.body.filepath;
  let contents = req.body.contents;
  fs.writeFile(filepath, contents, function(err) {
    if (err) {
      res.status(500);
      res.json({ message: 'Couldn\'t save file because: ' + err.message });
    } else {
      res.json({ message: 'File ' + filepath + ' saved.' });
    }
  });
});

app.listen(3000, function() {
  console.log('Example app listening on port 3000!');
});
