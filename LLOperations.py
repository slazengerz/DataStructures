## from <filename> import <clasname> as <alias>

from LLNode import Node
from LLConstructor import LinkedList as LLConstructor
from GraphsVisualization.DirectedGraphs import PlotGraph


pltgraph=PlotGraph()
linkedlist=LLConstructor(3)
##print(linkedlist.head.value)

###id print the memory location , in this example, head is the variable containing memory location of the node.
##print(id(linkedlist.head))
linkedlist.append(8)
linkedlist.append(5)
linkedlist.append(10)
linkedlist.append(2)
linkedlist.append(1)

linkedlist.partition_list(5)

#pltgraph.plotGraph(linkedlist)


pltgraph.plotGraph(linkedlist)