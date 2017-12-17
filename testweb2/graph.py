from graph_tool.all import *
import sys

g = Graph()
nodesNum = int(sys.argv[1])
for i in range(nodesNum):
	g.add_vertex()
	print(g.vertex_index)
graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18, output_size=(200, 200), output="draw.png")
