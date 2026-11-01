import pytest

from lab.cli import main

SUBCOMMANDS = ("data", "train", "evaluate", "run")


def test_help_lists_all_subcommands(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(["--help"])

    assert exit_info.value.code == 0
    help_text = capsys.readouterr().out
    for subcommand in SUBCOMMANDS:
        assert subcommand in help_text


@pytest.mark.parametrize("subcommand", ["data", "train", "evaluate"])
def test_unimplemented_step_fails_with_hint(subcommand, capsys):
    exit_code = main([subcommand])

    assert exit_code == 1
    assert "noch nicht implementiert" in capsys.readouterr().err


def test_run_requires_config_path(capsys):
    with pytest.raises(SystemExit) as exit_info:
        main(["run"])

    assert exit_info.value.code == 2
    assert "config" in capsys.readouterr().err
