# -*- encoding: utf-8 -*-
"""
hio.base Package
"""

import sys

IS_PYODIDE = "emscripten" in sys.platform

from .tyming import Tymist, Tymee, Tymer
from .doing import Doist, doize, doify, Doer, DoDoer
from .filing import openFiler, Filer, FilerDoer
from .webduring import WebSubDb, WebDuror, openWebDuror
from .subering import (Duror, SuberBase, Suber, IoSuber, IoSetSuber,
                       DomSuberBase, DomSuber, DomIoSuber, DomIoSetSuber, Subery)

if not IS_PYODIDE:
    from .during import openDuror
    from .multidoing import Bosser, Crewer, TagDex
