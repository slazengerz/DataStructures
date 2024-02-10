
import matplotlib.pyplot as plt
import networkx as nx 
import numpy as np

class PlotGraph:

    noOfTimesCalled=0
    def plotGraph(self,linkedList):
        ###using noOfTimesCalled print multiple graphs in 1 go without overlap
        
        self.noOfTimesCalled-=1
        print(f'---printing::{self.noOfTimesCalled} iteration')

        value=PlotGraph.LLtoListOfTuples(self,linkedList)
        color_map=[]
        G = nx.DiGraph() 
        G.add_edges_from(value) 
        pos={}
        j=0
        pos['H']=np.array([0, 0.002]) 
        for i in G.nodes:
            if i not in ['H','T']:
                color_map.append('green')
                pos[i]=np.array([j, .005*self.noOfTimesCalled]) 
                j+=1
            else:
                color_map.append('red')
        pos['T']=np.array([j-1, 0.002]) 
        nx.draw_networkx(G,pos,node_color=color_map) 
    
    ###Convert Linkedlist to listoftuples for displaying 
    def LLtoListOfTuples(self,list):
        listoftuples=[]
        temp=list.head
        pre=list.head
        listoftuples.append(('H',list.head.value))
        while temp.next:
            pre=temp
            temp=temp.next
            listoftuples.append((pre.value,temp.value))
        listoftuples.append(('T',list.tail.value))
        return listoftuples
