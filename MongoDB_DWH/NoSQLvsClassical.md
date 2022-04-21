# Gegenüberstellung NoSQL vs Relationale Datenbank

MongoDB benutzt das JSON-Format und definiert dabei kein starres Schema, was eine hohe Flexibilität bietet. 
Im Gegensatz dazu muss bei der relationalen Datenbank das Schema definiert werden, bevor Daten eingesetzt werden können.
Relationale Datenbanken sind also sehr gut darin Datenintegrität sicherzustellen und sind daher vor allem für Transaktionen gut geeignet (OLTP).

Für große Datenmengen kann eine NoSQL wie MongoDB aber sogar Performance Vorteile mit sich bringen, 
lediglich bei der Aggregation sind die herkömmlichen Datenbanken schneller. 
> S. Chickerur, A. Goudar and A. Kinnerkar, "Comparison of Relational Database with Document-Oriented Database (MongoDB) for Big Data Applications," 2015 8th International Conference on Advanced Software Engineering & Its Applications (ASEA), 2015, pp. 41-47, doi: 10.1109/ASEA.2015.19.

## Aspekte bei der Implementierung
Da der Aufbau eines DWHs relativ komplex sein kann, ist es ein Hindernis von Anfang an das Schema der Daten festlegen zu müssen, 
wodurch zukünftige Änderungen immer nur aufwändig zu repräsentieren sind. 
Das bedeutet das sehr viel Geld und Zeit in den Aufbau dieser Systeme gesteckt werden muss, 
bevor es überhaupt möglich ist einen einfachen Report generieren zu können.

Mit der Nutzung von NoSQL Datenbanken könnte es leichter möglich sein ein agiles Vorgehen zu nutzen, 
ohne sich von Anfang an auf eine Struktur festlegen zu müssen.

### Daten Relational -> NoSQL
Um Daten aus einer relationalen Datenbank nach MongoDB zu exportieren, müssen diese de-normalisiert werden.
De-normalisierte Daten machen die Abfragen einfacher, es bringt allerdings einige Herausforderungen mit sich die De-normalisierung richtig durchzuführen.
1:N Beziehungen sind dabei relativ trivial zu denormalisieren, während selbst-referenzierende Daten nicht komplett aufgelöst werden können.
M:N Beziehungen sollten nicht automatisch aufgelöst werden, da hierbei riesige, aber unnütze Datenmengen entstehen können.
Die größte Schwierigkeit ist dabei der Umgang mit numerischen Daten, da diese nicht redundant im Data Mart abgelegt werden sollten, 
aber durch die De-normalisierung oftmals dupliziert werden.

### DWH Design
Das DWH-Design sollt unter Umständen von der Häufigkeit mit der sich die Dimensionsdaten ändern, abhängig gemacht werden.
Da NoSQL-basierte Data Marts die beschreibenden Daten de-normalisiert speichern, können die entsprechenden
Attribute in nahezu jedem gespeicherten Dokument auftauchen. Ändern sich die Dimensionsdaten regelmäßig, 
so kann es zur Herausforderung werden eine passende Datenaktualisierungsstrategie zu finden, 
wenn nicht jedes Mal alle Daten neu geschrieben werden sollen.
Zudem kann es vorkommen, dass Aggregationen nicht von den Reporting Tools berechnet werden können und stattdessen im Data Mart als vorkalkulierte Werte gespeichert werden müssen.
In diesem Fall droht dann schnell eine Inkonsistenz, wenn Daten aktualisiert werden.

## Volltextsuche
Mit MongoDB ist es möglich eine Volltextsuche für die Dokumente zu integrieren. 
Es ist zwar technische möglich eine relationale Datenbank so zu indexieren, 
allerdings müssten dann jeweils aufwändige Joins gemacht werden, 
um die Daten zusammenzuführen, was das ganze kaum Praktikabel macht.
Da bei MongoDB einfach die ganzen Dokumente gespeichert werden, kann eine Google ähnliche Suche gebaut werden. 
Ein Beispiel: Es wird nach Otto gesucht und die Person Hannes gefunden, weil sie einen Hund namens Otto hat.

> Zane Bicevska, Ivo Oditis, Towards NoSQL-based Data Warehouse Solutions, Procedia Computer Science, Volume 104, 2017, Pages 104-111, ISSN 1877-0509
