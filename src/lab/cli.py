"""Startkommando `lab` mit den getrennten Schritten des Labs."""

import argparse
import sys
from pathlib import Path

# Welches Issue den jeweiligen Schritt mit Logik füllt.
PENDING_STEPS = {
    "data": "LAB-02",
    "train": "LAB-03",
    "evaluate": "LAB-03",
    "run": "LAB-03",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lab",
        description="Reproduzierbare ML-Experimente: Daten, Training, Evaluation.",
    )
    subcommands = parser.add_subparsers(dest="command", required=True, metavar="<befehl>")

    subcommands.add_parser("data", help="Datensatz laden, prüfen und Datenprofil schreiben")
    subcommands.add_parser("train", help="Modelle auf der Trainingsmenge trainieren")
    subcommands.add_parser("evaluate", help="Modelle einmalig auf der Testmenge bewerten")
    run = subcommands.add_parser("run", help="Vollständigen Lauf für eine Konfiguration ausführen")
    run.add_argument("config", type=Path, help="Pfad zur Konfigurationsdatei (TOML)")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    issue = PENDING_STEPS[args.command]
    print(f"lab {args.command}: noch nicht implementiert (folgt mit {issue}).", file=sys.stderr)
    return 1
