const express = require('express');
const app = express();

app.get('/add', (req, res) => {
  const a = parseFloat(req.query.a || 0);
  const b = parseFloat(req.query.b || 0);
  res.json({ result: a + b });
});

if (require.main === module) {
  app.listen(3000, () => console.log('Node service listening on 3000'));
}

module.exports = app;
