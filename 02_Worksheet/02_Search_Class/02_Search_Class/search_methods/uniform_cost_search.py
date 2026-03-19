
from utils.node_priority_queue import NodePriorityQueue
from search_methods.graph_search import GraphSearch
from search_methods.node import Node
from agents.state import State


class UniformCostSearch(GraphSearch):

    def __init__(self):
        super().__init__()
        self._frontier = NodePriorityQueue()

    # TODO
    # f = g
    def add_successor_to_frontier(self, successor: State, parent: Node) -> None:
        g = parent.g + successor.action.cost #cost of the parent + cost of going to the next node

        print("Frontier in the beginning: ", str(self._frontier))

        #If the successor is not on explored states or frontier (arrived states but not explored)
        if successor not in self._frontier:
            if successor not in self._explored:
                #Add to frontier
                self._frontier.append(Node(successor, parent, g=g, f=g))
        #If cost is lower than the successor cost
        elif g < self._frontier[successor].g:
            #deletes successor from the frontier
            del self._frontier[successor]
            #adds node to the frontier
            self._frontier.append(Node(successor, parent, g=g, f=g))

    def __str__(self):
        return "Uniform cost search"
