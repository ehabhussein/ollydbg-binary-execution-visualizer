#!/usr/bin/env python

import pygraphviz as pgv
from sys import argv,exit

if len(argv) < 2:
	print """
usage:
python eip-tracer.py nodes.txt graph-layout output.ext length-of-nodes-apart

graph layout:
dot
"hierarchical" or layered drawings of directed graphs. This is the default tool to use if edges have directionality.

neato
"spring model'' layouts.  This is the default tool to use if the graph is not too large (about 100 nodes) and you don't know anything else about it. Neato attempts to minimize a global energy function, which is equivalent to statistical multi-dimensional scaling.

fdp
"spring model'' layouts similar to those of neato, but does this by reducing forces rather than working with energy.

sfdp
multiscale version of fdp for the layout of large graphs.

twopi
radial layouts, after Graham Wills 97. Nodes are placed on concentric circles depending their distance from a given root node.

circo
circular layout, after Six and Tollis 99, Kauffman and Wiese 02. This is suitable for certain diagrams of multiple cyclic structures, such as certain telecommunications networks.


Extensions

canon cmap cmapx cmapx_np dot eps fig gd gd2 gif gv imap imap_np ismap jpe jpeg jpg pdf plain plain-ext png ps ps2 svg svgz tk vml vmlz vrml wbmp x11 xdot xlib

length of nodes apart
0 to 10 (prefered 3)

"""
	exit()
 
arr = []
arr.append("START")
G = pgv.AGraph(strict=False,directed=True)
for i,j in enumerate(open(argv[1],'r').xreadlines()):
	
	arr.append(j.strip())
	#G.add_edge()
#G.add_edge("START",arr[0])
for i,j in enumerate(arr):
    try:
    	G.add_edge(arr[i],arr[i+1],taillabel=i)
    except IndexError:
	G.add_edge(arr[i],"END")
G.graph_attr['label']='Ollydbg Binary visualizer'
G.node_attr['shape']='square'
G.node_attr['color']='orange'
#G.graph_attr['concentrate']='true'
G.edge_attr['len']=argv[4]
#G.graph_attr['nojustify']='true'
#G.layout()
G.layout(prog=argv[2])
#G.draw('done2.png')
G.draw(argv[3])

