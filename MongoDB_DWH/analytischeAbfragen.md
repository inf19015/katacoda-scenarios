# Analytische Abfragen
Nun zu einigen beispielhaften Abfragen:

## Bisheriger Gesamtumsatz:
`db.person.aggregate([
    {
        $unwind: "$Orders"
    },
    {
        $unwind: "$Orders.items"
    },
    {
        $addFields: {
            "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
        }
    },
    {
        $group: {
            _id: "",
            "Gesamtumsatz": { $sum: "$Orders.items.sum" }
        }
    }
])`{{execute}}

## Umsatz pro Person
`db.person.aggregate([
    {
        $unwind: "$Orders"
    },
    {
        $unwind: "$Orders.items"
    },
    {
        $addFields: {
            "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
        }
    },
    {
        $group: {
            _id: "$_id",
            "Umsatz": { $sum: "$Orders.items.sum" }
        }
    },
    {
        $sort: {
            Umsatz: -1
        }
    }
])`{{execute}}

## Durchschnittlicher Umsatz pro Bestellung
`db.person.aggregate([
    {
        $unwind: "$Orders"
    },
    {
        $unwind: "$Orders.items"
    },
    {
        $addFields: {
            "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
        }
    },
    {
        $group: {
            _id: "",
            "avgUmsatz": { $avg: "$Orders.items.sum" }
        }
    },
    {
        $sort: {
            avgUmsatz: -1
        }
    }
])`{{execute}}

## Durchschnittlicher Umsatz pro Person
`db.person.aggregate([
    {
        $unwind: "$Orders"
    },
    {
        $unwind: "$Orders.items"
    },
    {
        $addFields: {
            "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
        }
    },
    {
        $group: {
            _id: "$_id",
            "Umsatz": { $sum: "$Orders.items.sum" }
        }
    },
    {
        $group: {
            _id: "",
            "avgUmsatz": { $avg: "$Umsatz" }
        }
    },
    {
        $sort: {
            avgUmsatz: -1
        }
    }
])`{{execute}}
