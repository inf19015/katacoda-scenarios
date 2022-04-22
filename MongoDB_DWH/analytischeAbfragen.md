# Analytische Abfragen
Nun zu einigen beispielhaften Abfragen. Da alle Informationen wie Bestellungen direkt im Dokument der Person gespeichert sind, 
ist es nicht nötig die bei relationalen Datenbanken notwendigen Joins zu verwenden. 
Stattdessen müssen wir aber für Aggregationen bei verschachtelten Listen den Datensatz verflachen, 
also den Datensatz so transformieren, dass für jeden Eintrag der Liste ein eigener Eintrag existiert.
Dies passiert mit `$unwind`

## Bisheriger Gesamtumsatz:
`db.person.aggregate([
    { $unwind: "$Orders"},
    { $unwind: "$Orders.items"},
    {$addFields: {
        "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
    }},
    { $group: {
        _id: "",
        "Gesamtumsatz": { $sum: "$Orders.items.sum" }
    }}
])`{{execute}}

## Umsatz pro Person
`db.person.aggregate([
    { $unwind: "$Orders"},
    { $unwind: "$Orders.items"},
    {$addFields: {
        "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
    }},
    {
        $group: {
            _id: "$_id",
            "Umsatz": { $sum: "$Orders.items.sum" },
            "avgUmsatz": { $avg: "$Orders.items.sum" }
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
    { $unwind: "$Orders"},
    { $unwind: "$Orders.items"},
    {$addFields: {
        "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
    }},
    {$group: {
        _id: "$Orders",
        "Umsatz": { $sum: "$Orders.items.sum" }
    }},
    {$group: {
        _id: "",
        "avgUmsatz": { $avg: "$Umsatz" }
    }},
    { $sort: { avgUmsatz: -1 }}
])`{{execute}}


## Für alle Personen die in "North Star Elementary" auf der Schule waren, alle besuchten Schulen anzeigen
Diese Anfrage würde in SQL sehr komplex ausfallen, man müsste erst die passenden schulen finden, 
auf die Personen joinen und dann wieder für jede Personen alle besuchten Schulen finden.
Mit MongoDB dagegen ist das ein Einzeiler:
`db.person.find({"Education.school": "North Star Elementary"}, { "Education.school": 1})`{{execute}}

## Zusammenhang Umsatz mit Hobby
Es soll für jedes Hobby der Gesamtumsatz, sowie der durchschnittliche Bestellwert gefunden werden. 
`db.person.aggregate([
    {$unwind: "$Orders"},
    {$unwind: "$Orders.items"},
    {$addFields: {
        "Orders.items.sum": { $multiply: [ "$Orders.items.count", "$Orders.items.price"] }
    }},
    {$group: {
        _id: "$Orders",
        "Bestellwerte": { $sum: "$Orders.items.sum" },
        "Hobbies": { $addToSet: "$Hobbies"}
    }},
    {$unwind: "$Hobbies"},
    {$unwind: "$Hobbies"},
    {$group: {
        _id: "$Hobbies",
        "GesamtUmsatz": { $sum: "$Bestellwerte" },
        "avgBestellwert": { $avg: "$Bestellwerte" }
    }},
    {$sort: {avgBestellwert: -1}}
])`{{execute}}
