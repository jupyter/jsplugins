# -*- coding: utf-8 -*-
"""
Online Python Tutor magic function for the Notebook.

Authors:
* Brian Granger
* Philip Guo
"""
#-----------------------------------------------------------------------------
# Copyright (C) 2012, IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from __future__ import print_function

import os
import re
import sys
import time

from IPython.core import display
from IPython.core import magic_arguments
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.displaypub import publish_json

from zmq.utils import jsonapi

import pg_logger

@magics_class
class PyTutorMagics(Magics):

    def __init__(self, shell):
        super(PyTutorMagics,self).__init__(shell)

    @cell_magic
    def pytutor(self, line, cell):
        code, trace = pg_logger.exec_script_str(cell, False)
        result = dict(code=code, trace=trace, handler='pytutor')
        data = jsonapi.dumps(result)
        publish_json(data)


_loaded = False

def load_ipython_extension(ip):
    """Load the extension in IPython."""
    global _loaded
    if not _loaded:
        ip.register_magics(PyTutorMagics)
        _loaded = True
