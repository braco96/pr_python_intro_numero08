# -*- coding: utf-8 -*-
import re
from pathlib import Path

def contar_lineas(path):
    p = Path(path)
    return 0 if not p.exists() else sum(1 for _ in p.open("r", encoding="utf-8"))

