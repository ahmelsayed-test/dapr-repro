const express = require('express');

const app = express();
app.use(express.json());

const port = 3000;

var orders = [
    {
        id: "1",
        name: "lightsaber replica",
        type: "collectable",
        price: "259.99"
    },
    {
        id: "2",
        name: "vader: litany",
        type: "music",
        price: "39.99"
    },
    {
        id: "3",
        name: "forgotten realms: exile",
        type: "book",
        price: "59.99"
    }
]

app.get('/orders', (_req, res) => {
    res.json(orders)
    console.log(`List of orders requested by ${_req.ip}`)
});

app.post('/orders', (req, res) => {
    orders.push(req.body)
    res.status(200).send("success")
    console.log(`Received new order from ${req.ip}, content: ${JSON.stringify(req.body)}`)
});

app.listen(port, () => console.log(`Node App listening on port ${port}!`));
