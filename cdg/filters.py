#
# Copyright (c) 2017 Brian J. Kidney
# Copyright (c) 2017 Jonathan Anderson
# All rights reserved.
#
# This software was developed by BAE Systems, the University of Cambridge
# Computer Laboratory, and Memorial University under DARPA/AFRL contract
# FA8650-15-C-7558 ("CADETS"), as part of the DARPA Transparent Computing
# (TC) research program.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import cdg.query


def apply(filter_spec, graph):
    '''
    Apply a filter like pred:read,write or succ:main to a graph.
    '''

    (name, arg) = filter_spec.split(':')

    if name == 'exclude':
        to_keep = arg.split(',')
        return exclude(graph, to_keep)

    elif name == 'pred':
        keep = set(arg.split(','))
        select_fn = graph.predecessors
        nodes = cdg.query.transitive_neighbours(graph, keep, select_fn)
        print('Keeping %d predecessors of %d nodes' % (len(nodes), len(keep)))

    elif name == 'succ':
        keep = set(arg.split(','))
        select_fn = graph.successors
        nodes = cdg.query.transitive_neighbours(graph, keep, select_fn)
        print('Keeping %d predecessors of %d nodes' % (len(nodes), len(keep)))














    return cdg.hot_patch(graph.subgraph(nodes))


def exclude(graph, to_exclude):
    result = graph.copy()

    for n in to_exclude:
        result.remove_node(n)

    print('Removed %d nodes, %d edges' % (
        len(graph.nodes) - len(result.nodes),
        len(graph.edges) - len(result.edges),
    ))

    return result


def intersection(G, H):
    R = G.full_copy()
    R.remove_nodes_from(n for n in G if n not in H)
    return R


def union(G, H):
    R = G.full_copy()
    R.add_edges_from(H.edges())
    return R
