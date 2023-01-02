import io
from random import randint
from unittest.mock import Mock
import grep


def test_count_pattern_in_file_GivenCaratAuthor_PrintsCountAndProvidedRegex(capfd, monkeypatch):
    input = ['^Author']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    grep.count_pattern_in_file()


    out, err = capfd.readouterr()
    assert "1798 lines" in out
    assert "^Author" in out

def test_count_pattern_in_file_GivenCaratXDash_PrintsCountAndProvidedRegex(capfd, monkeypatch):
    input = ['^X-']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    grep.count_pattern_in_file()


    out, err = capfd.readouterr()
    assert "14368 lines" in out
    assert "^X-" in out

def test_count_pattern_in_file_GivenJavaDollar_PrintsCountAndProvidedRegex(capfd, monkeypatch):
    input = ['java$']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    grep.count_pattern_in_file()


    out, err = capfd.readouterr()
    assert "4175 lines" in out
    assert "java$" in out