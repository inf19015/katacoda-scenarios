# Erste Abfrage
Um sich auf die MongoDB zu verbinden, müssen wir uns in die MongoDB Konsole einloggen:
`docker exec -it dwh_mongo_1 mongosh`{{execute}}

Die Datenbank auswählen:
`use dwh`{{execute}}

Und eine Testabfrage auf einen Datensatz ausführen:
`db.person.findOne()`{{execute}}
