# CS4102 Spring 2020 -- Homework 8
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: FSK2PD
# Collaborators: N/A
# Sources: Introduction to Algorithms, Cormen
#################################
import networkx as nx

class TilingDino:
    def __init__(self):
        self.isValid = False
    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):

        #builds matrix from input to later use to build bipartite graph
        def buildMatrix(lines):
            rows,cols = len(lines),len(lines[0])
            matrix = [["" for i in range(cols)] for j in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    matrix[i][j] = lines[i][j]
            #marking all possible adjacent nodes with "-"
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] == ".":
                        matrix[i][j] = "."
                    elif (i%2 != 0 and j%2 != 0):
                        matrix[i][j] = "-"
                    elif (i%2 != 0 and j%2 == 0):
                        matrix[i][j] = "#"    
                    elif (i%2 == 0 and j%2 == 0):
                        matrix[i][j] = "-"
                    elif (i%2 == 0 and j%2 != 0):
                        matrix[i][j] = "#"            
            return matrix
        #function to build bipartite graph
        def makeGraph(matrix):
            rows,cols = len(matrix),len(matrix[0])
            graph = nx.Graph()
            for i in range(rows):
                for j in range(cols):
                    if(matrix[i][j] == "#"):
                        graph.add_node(str(j) + " " + str(i), bipartite = 0)
                    elif(matrix[i][j] == "-"):
                        graph.add_node(str(j) + " " + str(i), bipartite = 1)

            #checking all adjacent nodes to see if there exists a matching node and then building path
            #also checking edge cases to ensure no index out of range errors
            #probably could have built graph with a queue but was struggling to figure out how to manipulate it
            for i in range(rows):
                for j in range(cols):
                    if (i == 0 and j == 0):
                        if(matrix[i][j] == "#" and matrix[i][j+1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j+1) + " " + str(i))
                        if(matrix[i][j] == "#" and matrix[i+1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i+1))

                    elif (i == rows -1 and j == 0):
                        if(matrix[i][j] == "#" and matrix[i-1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i-1))
                        if(matrix[i][j] == "#" and matrix[i][j+1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j+1) + " " + str(i))

                    elif (j == cols -1 and i == 0):
                        if(matrix[i][j] == "#" and matrix[i+1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i+1))
                        if(matrix[i][j] == "#" and matrix[i][j-1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j-1) + " " + str(i))  

                    elif (i == rows -1 and j == cols-1):
                        if(matrix[i][j] == "#" and matrix[i-1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i-1))
                        if(matrix[i][j] == "#" and matrix[i][j-1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j-1) + " " + str(i)) 

                    elif (j != cols-1 and j!=0 and i == 0):
                        if(matrix[i][j] == "#" and matrix[i][j-1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j-1) + " " + str(i))
                        if(matrix[i][j] == "#" and matrix[i+1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i+1))
                        if(matrix[i][j] == "#" and matrix[i][j+1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j+1) + " " + str(i))

                    elif (i != 0 and j== cols -1 and i != rows-1): 
                        if(matrix[i][j] == "#" and matrix[i-1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i-1))
                        if(matrix[i][j] == "#" and matrix[i][j-1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j-1) + " " + str(i))
                        if(matrix[i][j] == "#" and matrix[i+1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i+1))

                    elif (j != cols-1 and j!=0 and i == rows-1):
                        if(matrix[i][j] == "#" and matrix[i-1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i-1))
                        if(matrix[i][j] == "#" and matrix[i][j+1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j+1) + " " + str(i))
                        if(matrix[i][j] == "#" and matrix[i][j-1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j-1) + " " + str(i))

                    elif (i != 0 and j==0 and i != rows-1):
                        if(matrix[i][j] == "#" and matrix[i-1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i-1))
                        if(matrix[i][j] == "#" and matrix[i][j+1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j+1) + " " + str(i))
                        if(matrix[i][j] == "#" and matrix[i+1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i+1))

                    else:
                        if(matrix[i][j] == "#" and matrix[i-1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i-1))
                        if(matrix[i][j] == "#" and matrix[i][j-1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j-1) + " " + str(i))
                        if(matrix[i][j] == "#" and matrix[i+1][j] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j) + " " + str(i+1))
                        if(matrix[i][j] == "#" and matrix[i][j+1] == "-"):
                            graph.add_edge(str(j) + " " + str(i), str(j+1) + " " + str(i))

            return graph

        #if the input does not contain # then it is not valid
        p = "#"
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if p == lines[i][j]:
                    self.isValid = True
                    break
        if self.isValid:
            grid = buildMatrix(lines)
            graph = makeGraph(grid)
        
            #establish bipartite sets
            left = {n for n, d in graph.nodes(data = True) if d['bipartite'] == 0}
            #used maximum_matching algorithm to match nodes
            match = nx.bipartite.maximum_matching(graph,left)

            ans = []
            #if graph all nodes are matched 1 to 1 then return coordinates else return impossible
            if nx.number_of_nodes(graph)/2 == len(left):
                for i in match:
                    if i in left:
                        ans.append(i + " " + match[i])
                return ans
            return ["impossible"]
        else:
            return ["impossible"]