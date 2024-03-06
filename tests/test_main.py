import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_contar_lineas(tmp_path):
    f = tmp_path / "x.txt"
    f.write_text("a\n b\n c", encoding="utf-8")
    assert mod.contar_lineas(f) == 2
    assert mod.contar_lineas(tmp_path / "no.txt") == 0
