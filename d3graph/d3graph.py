# -*- coding: utf-8 -*-
"""
D3 Graph visualizations for NetworkX.

Authors:
* Brian Granger
"""
#-----------------------------------------------------------------------------
# Copyright (C) 2012, IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from IPython.core.displaypub import publish_json

import networkx as nx
from networkx.readwrite import json_graph

from zmq.utils import jsonapi

def graph_to_json(G):
    d = json_graph.node_link_data(G) # node-link format to serialize
    d['handler'] = 'd3graph'
    data = jsonapi.dumps(d)
    return data

_loaded = False

def load_ipython_extension(ip):
    """Load the extension in IPython."""

    global _loaded
    if not _loaded:
        json_formatter = ip.display_formatter.formatters['application/json']

        json_formatter.for_type_by_name(
            'networkx.classes.graph', 'Graph', graph_to_json
        )
        _loaded = True