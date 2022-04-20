# Beispieldatensatz
Da MongoDB mit JSON als Format arbeitet, liegt auch der Beispieldatensatz im JSON-Format vor.

Schau dir den verwendeten Datensatz ruhig mal an:
`head ./data_persons_merged`{{execute}}

Dies ist auch schon der erste große Vorteil von diesen Datenbanken: JSON-Datensätze können direkt übernommen werden, 
ohne das diese in viele kleine Tabellen mit Primär- und Fremdschlüsseln aufgeteilt werden müssen. 
Dies sollte also den ETL-Prozess für solche Daten sehr vereinfachen. 

[//]: # (Da für analytische Abfragen sowieso normalerweise stark denormalisiert wird,)
