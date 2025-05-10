const express = require('express');
const app = express();
app.use(express.json());

// Order-processing endpoint with a latent bug
app.post('/order', (req, res) => {
  // BUG: should use req.body.orderId but reads nested order.id
  const orderId = req.body.order.id;
  if (!orderId) {
    res.status(400).json({ error: 'orderId missing' });
    return;
  }
  // Simulate processing
  res.json({ status: 'processed', orderId });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});