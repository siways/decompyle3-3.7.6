"""
  Copyright (c) 2015, 2018, 2020-2021 by Rocky Bernstein
  Copyright (c) 2000 by hartmut Goebel <h.goebel@crazy-compilers.com>
  Copyright (c) 1999 John Aycock

  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the
  "Software"), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so, subject to
  the following conditions:

  The above copyright notice and this permission notice shall be
  included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

  NB. This is not a masterpiece of software, but became more like a hack.
  Probably a complete rewrite would be sensefull. hG/2000-12-27
"""

import sys

__docformat__ = "restructuredtext"

from decompyle3.version import __version__  # noqa
from xdis import PYTHON_VERSION_TRIPLE

PYTHON_VERSION_STR: str = "%s.%s" % (sys.version_info[0], sys.version_info[1])

IS_PYPY: bool = "__pypy__" in sys.builtin_module_names

if hasattr(sys, "setrecursionlimit"):
    # pyston doesn't have setrecursionlimit
    sys.setrecursionlimit(5000)

import decompyle3.semantics.pysource
import decompyle3.semantics.fragments

# Export some functions
from decompyle3.main import decompile_file

# Convenience functions so you can say:
# from decompyle3 import (code_deparse, deparse_code2str)

deparse_code2str = decompyle3.semantics.pysource.deparse_code2str
code_deparse = decompyle3.semantics.pysource.code_deparse
