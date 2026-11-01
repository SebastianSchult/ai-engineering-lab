# AI Engineering Lab

Lern-Lab für reproduzierbare ML-Experimente. Der erste Fall ist die Vorhersage der Betondruckfestigkeit.

## Daten

**Mischung**:
Eine Zeile des Datensatzes: Rezeptur plus Alter und gemessene Festigkeit.
_Avoid_: Sample, Datenpunkt

**Rezeptur**:
Die sieben Mengenangaben einer Mischung ohne Alter. Mehrere Mischungen können dieselbe Rezeptur haben.
_Avoid_: Mix, Zusammensetzung

**Merkmal**:
Eine Eingabespalte, die das Modell sehen darf.
_Avoid_: Feature, Variable, Attribut

**Zielgröße**:
Die vorherzusagende Druckfestigkeit in MPa.
_Avoid_: Label, Target, y

**Datenprofil**:
Kennzahlen über den geladenen Datensatz, die vor jeder Modellierung erhoben werden.

## Aufteilung

**Trainingsmenge**:
Der Teil der Daten, auf dem gefittet und per Kreuzvalidierung ausgewählt wird.

**Testmenge**:
Der vor jeder Analyse abgetrennte Teil, der genau einmal zur Schlussbewertung dient.
_Avoid_: Validierungsset (das ist ein Fold innerhalb der Trainingsmenge)

**Fold**:
Ein Teilstück der Trainingsmenge in der Kreuzvalidierung.

## Experimente

**Referenzvorhersage**:
Ein Modell, das ohne Merkmale vorhersagt, nämlich den Mittelwert oder Median der Trainingsmenge.
_Avoid_: Dummy, naive Vorhersage

**Lauf**:
Eine Ausführung des Startkommandos mit genau einer Konfiguration, inklusive Ergebnisordner.
_Avoid_: Run, Job

**Experiment**:
Eine Konfiguration mit einer Lernfrage. Sie kann mehrere Modelle vergleichen.

**Demo-Lauf**:
Ein absichtlich ungültiger Lauf zur Demonstration eines Fehlers. Er ist nie Teil des Ergebnisprotokolls.
_Avoid_: Test-Lauf

**Lauf-Bericht**:
Die automatisch erzeugte Zusammenfassung eines einzelnen Laufs.

**Ergebnisprotokoll**:
Die von Sebastian kommentierte Zusammenfassung gültiger Läufe.
_Avoid_: Log, Report

**Residuum**:
Tatsächliche minus vorhergesagte Festigkeit einer Mischung.

**Data Leakage**:
Information aus der Testmenge oder der Zielgröße, die beim Training sichtbar war.
