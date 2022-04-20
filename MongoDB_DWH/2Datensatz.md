# Beispieldatensatz
Da MongoDB mit JSON als Format arbeitet, liegt auch der Beispieldatensatz im JSON-Format vor.

Dies ist auch schon der erste große Vorteil von diesen Datenbanken: JSON-Datensätze können direkt übernommen werden,
ohne das diese in viele kleine Tabellen mit Primär- und Fremdschlüsseln aufgeteilt werden müssen.
Dies sollte also den ETL-Prozess für solche Daten sehr vereinfachen.

Der Datensatz enthält Personen, welche jeweils mehrere Hobbies haben können. 
Zudem sind die bisher besuchten Schulen, sowie Bestellungen bei einem Fahrradladen enthalten.

Schau dir den verwendeten Datensatz ruhig mal an:
`less ./data_persons_merged`{{execute}}
(Um die Ansicht zu schließen, `q`{{execute}} drücken)





[//]: # (Da für analytische Abfragen sowieso normalerweise stark denormalisiert wird,)
