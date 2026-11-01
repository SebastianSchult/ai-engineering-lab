# AGENTS.md – ai-engineering-lab

## Zweck

Lern-Lab. Sebastian will jedes Ergebnis selbst verstehen und erklären. Geschwindigkeit ist zweitrangig.

## Vor jeder Aufgabe lesen

- `GLOSSARY.md`: Begriffe verwenden, keine Synonyme
- `docs/adr/`: keine Entscheidung stillschweigend überschreiben
- das zugehörige Issue inkl. Abnahmekriterien

## Aufgaben des Agenten

- Projektgerüst, CLI, Konfigurationsparsing, Bericht-Formatierung
- Tests an den vereinbarten Seams schreiben, test-first: `run_experiment(config)` und Datenschritt
- Code-Review und Erklärungen auf Deutsch, mit konkretem Beispiel
- ML-Kernfunktionen (Aufteilung, Pipeline, Evaluation) schreibt Sebastian. Der Agent reviewt, erklärt und schreibt die Tests dafür, aber nicht die Implementierung, außer das Issue sagt ausdrücklich etwas anderes.

## Schreibgrenzen

- Darf ändern: `src/`, `tests/`, `configs/`, `README.md`, `.github/`, `pyproject.toml` (ohne neue Abhängigkeiten)
- Nur nach Rückfrage: `GLOSSARY.md`, neue Abhängigkeiten, `uv.lock`, neue ADRs
- Darf NICHT ändern: `data/`, `runs/`, bestehende ADRs, Abschnitte „Meine Erklärung“ in `RESULTS.md`, Ergebnisse in `HANDOFF.md`
- Seed, Testanteil und Aufteilungsstrategie nur per ADR ändern

## Harte Regeln

- Die Testmenge nie zur Modellwahl, Merkmalsauswahl oder Schwellenfindung nutzen
- Jede Vorverarbeitung gehört in eine Pipeline
- Demo-Läufe schreiben nur nach `runs/_invalid_demo/` und tragen ein Warnbanner; ihre Zahlen nie in gültige Tabellen übernehmen
- Keine Ergebnisse oder Kennzahlen erfinden oder vorab eintragen
- Kein Push auf `main` ohne Auftrag; Arbeit auf Feature-Branches mit PR
- Ein Issue pro Session, Changes reviewbar halten (ca. 300 LOC)

## Prüfkommandos

Vor jedem Commit lokal ausführen; dieselben Schritte laufen in der CI (`.github/workflows/ci.yml`):

```bash
uv sync --locked
uv run ruff check
uv run ruff format --check
uv run pytest
```

Tests brauchen keinen Netzwerkzugriff. Neue Tests nutzen Fixtures statt echter Downloads.

## Agent skills

### Issue tracker

Issues und Specs liegen als GitHub Issues in `SebastianSchult/ai-engineering-lab`. See `docs/agents/issue-tracker.md`.

### Triage labels

Die fünf Standard-Rollen mit Standard-Labels (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: ein `GLOSSARY.md` und `docs/adr/` im Repo-Root. See `docs/agents/domain.md`.
