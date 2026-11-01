# ai-engineering-lab

Ein schlankes, reproduzierbares Python-Lab, in dem ich ML-Experimente selbst ausführe, vergleiche und erkläre. Phase 0 meines Lernpfads zu AI Product Engineering.

**Status:** Projektgerüst steht (LAB-01). Die Schritte selbst folgen ab LAB-02.

## Start

Voraussetzung: [uv](https://docs.astral.sh/uv/). Python 3.13 wird von uv bei Bedarf installiert.

```bash
uv sync
uv run lab --help
```

## Worum es geht

Erstes Problem: Vorhersage der Betondruckfestigkeit (MPa) aus der Mischung. Eine Referenzvorhersage (Mittelwert/Median der Trainingsmenge) wird mit einer linearen Regression verglichen. Primäre Metrik ist der MAE. Vorverarbeitung läuft ausschließlich auf Trainingsdaten. Dazu kommen eine Fehleranalyse und drei Lernexperimente: Merkmalsauswahl, Modellkomplexität und eine klar als ungültig markierte Data-Leakage-Demonstration.

Bewusst nicht enthalten: Weboberfläche, Experimenttracking-Server, ML-Plattform, GPU.

## Architektur in einem Absatz

Ein Python-Paket mit getrennten Schritten für Daten, Training und Evaluation, verkettet durch ein Startkommando. Jede Konfiguration (TOML) beschreibt genau ein Experiment. Ein Lauf schreibt Kennzahlen, Vorhersagen und einen Kurzbericht in einen eigenen Ordner. Vorverarbeitung und Modell stecken immer gemeinsam in einer scikit-learn-`Pipeline`. Ein Notebook dient nur der Erkundung.

```text
Konfiguration → Datenschritt (Download, Hash, Schema, Profil) → Aufteilung (Testmenge zuerst abtrennen)
             → Training (Kreuzvalidierung nur auf Trainingsmenge) → Evaluation (einmalig auf Testmenge)
             → Lauf-Bericht → Ergebnisprotokoll (RESULTS.md)
```

## Dokumente

- [AGENTS.md](AGENTS.md): Aufgaben- und Schreibgrenzen für KI-Agenten
- [GLOSSARY.md](GLOSSARY.md): Domänensprache
- `docs/adr/`: Architekturentscheidungen, sobald sie anfallen
- `RESULTS.md`: Ergebnisprotokoll, entsteht mit den ersten Läufen

Das Repo nutzt bewusst nur einen Teil meines Repository Starter Packs (kein ARCHITECTURE/ROADMAP/SECURITY/DEVSECOPS/QA_GUIDELINES), weil die volle Doku für ein Lern-Lab dieser Größe Overhead wäre.

## Daten

I-Cheng Yeh (1998): *Concrete Compressive Strength*. UCI Machine Learning Repository. DOI [10.24432/C5PK67](https://doi.org/10.24432/C5PK67). Lizenz: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Die Rohdaten werden nicht committet, sondern beim ersten Lauf heruntergeladen und per SHA-256 geprüft.
