# Graph implementation using an Adjacency List data structure with a dictionary.
# Each dictionary key represents a vertex, and its associated list contains neighboring vertices.
#This implementation contains methods for directed and undirected graphs. Usage of directed graph methods is specified in user code.
class Graph:
    """
    A class representing a graph.

    This class provides methods for adding vertices, adding edges, and performing various graph traversal and analysis operations.
    """
    def __init__(self):
        """
        Initialize an empty graph as an adjacency list.
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph if it doesn't already exist.

            Parameters: 
                vertex (any): The vertex to be added.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """
        Add an edge between two vertices, if not already connected.

            Parameters:
                vertex1 (any): The first vertex.
                vertex2 (any): The second vertex.
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        # if vertex1 not in self.graph[vertex2]:
        #     self.graph[vertex2].append(vertex1)


    def get_neighbours(self, vertex):
        """
        Print the neighbors of a given vertex.

            Parameters:
                vertex (any): The vertex to get neighbors for.
        """
        print(self.graph.get(vertex, []))

    def __str__(self):
        """
        Convert the graph to a string.

            Returns: 
                str: String representation of the graph.
        """
        result = []
        for vertex, neighbors in self.graph.items():
            result.append(f"{vertex}: {', '.join(neighbors)}")

        return "\n".join(result)
    
    def bfs_traversal(self, start_vertex):
        """
        Perform a breadth-first traversal of the graph.

            Parameters:
                start_vertex (any): The starting vertex for traversal.

            Returns: 
                list: List of vertices in BFS order.
        """
        visited = {start_vertex}
        queue = [start_vertex]
        result = []

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return result

    def dfs_traversal(self, start_vertex):
        """
        Perform a depth-first traversal of the graph.

            Parameters: 
                start_vertex (any): The starting vertex for traversal.

            Returns: 
                list: List of vertices in DFS order.
        """
        visited = {start_vertex}
        stack = [start_vertex]
        result = []

        while stack:
            vertex = stack.pop()
            result.append(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
        return result

    def count_of_nodes(self, level, start_vertex = None):
        """
        Count the number of nodes at a given level from a specified vertex.

            Parameters:
                level (int): The level to count nodes at.
                start_vertex (any): The starting vertex (default is the first vertex).

            Returns: 
                int: Number of nodes at the specified level.
        """
        if start_vertex == None:
            start_vertex = next(iter(self.graph.keys()), None)
        if start_vertex == None:
            return 0

        visited = {start_vertex}
        queue = [(start_vertex, 0)]
        count = 0

        while queue:
            vertex, current_level = queue.pop(0)

            if current_level == level:
                count += 1
            if current_level > level:
                break
            
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, current_level + 1))
        return count

    def traverse_components_if_exist(self):
        """
        Traverse and print separate components in the graph if they exist.
        """
        visited = set()
        components = []

        for vertex in self.graph:
            if vertex not in visited:
                component = self.dfs_traversal(vertex)
                components.append(component)
                visited.update(component)
        
        if len(components) == 1:
            print("The graph is entirely connected. Performing a traversal" "\n" "Traversal result:", components[0])

        else:
            print("There are seperate components.Performing seperate traversals")
            for i, component in enumerate(components):
                print(f"Component {i + 1}" "\n" "Traversal result:", component)
 


    def find_shortest_path(self, start, end):
        """
        Find the shortest path between two vertices using BFS.

            Parameters: 
                start (any): The starting vertex.
                end (any): The ending vertex.

            Returns: 
                list: List of vertices representing the shortest path.
        """
        if start not in self.graph or end not in self.graph:
            return None
        
        visited = {start}
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)

            if current == end:
                return path

            for neighbour in self.graph.get(current, []):
                if neighbour not in visited:
                    queue.append((neighbour, path + [neighbour]))
                    visited.add(neighbour)

    
    def all_possible_paths(self, start, end):    
        """
        Find all possible paths between two vertices using DFS.

            Paramenets:
                start (any): The starting vertex.
                end (any): The ending vertex.

            Returns: 
                list: List of all possible paths as lists of vertices.
        """
        if start not in self.graph or end not in self.graph:
            return None
        
        def dfs_paths(current, target, path):
            visited.add(current)
            path.append(current)

            if current == target:
                all_paths.append(path.copy())
            else:
                for neighbour in self.graph[current]:
                    if neighbour not in visited:
                        dfs_paths(neighbour, target, path)
            visited.remove(current)
            path.pop()


        visited = set()
        all_paths = []
        dfs_paths(start, end, [])
        return all_paths
    
    def has_cycle(self, start_vertex = None):
        """
        Checks if the graph has a cycle using DFS traversal.

        Parameters:
            start_vertex (any): The starting vertex for the traversal (default is the first vertex).

        Returns:
            bool: True if a cycle exists, False otherwise.
        """
        if start_vertex == None:
            start_vertex = next(iter(self.graph.keys()), None)
        if start_vertex == None:
            return False
        
        visited = {start_vertex}
        stack = [(start_vertex, None)] 

        while stack:
            vertex, parent = stack.pop()

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append((neighbour, vertex))
                elif neighbour != parent:
                    return True
        return False
    
    def has_cycle_directed(self):
        """
        Checks if the directed graph has a cycle using DFS traversal.

        Returns:
            bool: True if a cycle exists, False otherwise.
        """
        visited = set()
        rec_stack = set()

        def is_cyclic(vertex):
            """
            Recursive helper function to detect cycles in the graph.

            Parameters:
                vertex (any): The current vertex being explored.

            Returns:
                bool: True if a cycle is found, False otherwise.
            """
            if vertex in rec_stack:
                return True
            if vertex not in visited:
                visited.add(vertex)
                rec_stack.add(vertex)

            for neighbour in self.graph.get(vertex, []):
                if is_cyclic(neighbour):
                    return True
            rec_stack.remove(vertex)
            return False

        for vertex in self.graph:
            if is_cyclic(vertex):
                return True
        return False

    def topological_sort(self):
        """
        Performs a topological sort on a graph.

        Retruns:
            list: A list representing the topological order of vertices.
        """
        visited = set()
        result = []

        def top_sort_helper(vertex, visited, result):
            """
            Recursive helper function to perform DFS for topological sort.

            Parameters:
                vertex (any): The current vertex being explored.
                visited (set): Set of visited vertices.
                result (list): List to store the topological order.

            Returns:
                None
            """
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    top_sort_helper(neighbour, visited, result)
            result.insert(0, vertex)

        for vertex in self.graph:
            if vertex not in visited:
                top_sort_helper(vertex, visited, result)
        return result
    
    def khans_algorithm_directed(self):
        """
        Performs a topological sort using Khan's algorithm on a directed graph.

        Returns:
            list: The topologically sorted vertices or an empty list if the graph contains a cycle.
        """
        in_degree = {vertex: 0 for vertex in self.graph}
        queue = []
        result = []

        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                in_degree[neighbour] += 1

        for vertex in in_degree:
            if in_degree[vertex] == 0:
                queue.append(vertex)
        
        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbour in self.graph[vertex]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        if len(result) != len(self.graph):
            return []
        
        return result

    def kosaraju_algorithm(self):
        """
        Performs Kosaraju's algorithm to find strongly connected components(SCCs) in a graph.

        Returns:
            list of lists: List of strongly connected components.
        """
        def first_dfs(vertex, visited, stack):
            """
            Performs the first depth-first search (DFS) traversal to fill the stack.

            Parameters:
                vertex (any): The current vertex being explored.
                visited (set): Set of visited vertices.
                stack (list): List to store the finishing times of vertices.
            """
            visited.add(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    first_dfs(neighbour, visited, stack)
            stack.append(vertex)

        stack = []
        visited = set()
        for vertex in self.graph:
            if vertex not in visited:
                first_dfs(vertex, visited, stack)

        transposed_graph = {vertex: [] for vertex in self.graph}
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                transposed_graph[neighbour].append(vertex)

        def second_dfs(vertex, visited, component):
            """
            Performs the second depth-first search (DFS) traversal to identify components.

            Parameters:
                vertex (any): The current vertex being explored.
                visited (set): Set of visited vertices.
                component (list): List to store the current strongly connected component.
            """
            visited.add(vertex)
            component.append(vertex)
            for neighbour in transposed_graph[vertex]:
                if neighbour not in visited:
                    second_dfs(neighbour, visited, component)
            
        visited.clear()
        strongly_connected_components = []
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                current_component = []
                second_dfs(current_vertex, visited, current_component)
                strongly_connected_components.append(current_component)
        return strongly_connected_components
    
    def tarjan_algorithm(self):
        """
        Performs Tarjan's algorithm to find strongly connected components(SCCs) in a graph.

        Returns:
            list of lists: List of strongly connected components.
        """
        index_counter = [0]
        index = {}
        low_link = {}
        on_stack = set()
        stack = []
        result =[]

        def strongconnect(vertex):
            """
            Performs the depth-first search (DFS) and identifies strongly connected components(SCCs) starting from the given vertex.

            Parameters:
                vertex (any): The current vertex being explored.
            """
            index[vertex] = index_counter[0]
            low_link[vertex] = index_counter[0]
            index_counter[0] += 1
            stack.append(vertex)
            on_stack.add(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour not in index:
                    strongconnect(neighbour)
                    low_link[vertex] = min(low_link[vertex], low_link[neighbour])
                elif neighbour in on_stack:
                    low_link[vertex] = min(low_link[vertex], index[neighbour])

            if low_link[vertex] == index[vertex]: 
                component = []
                while True:
                    node = stack.pop()
                    on_stack.remove(node)
                    component.append(node)
                    if node == vertex: 
                        break
                result.append(component)

        for vertex in self.graph:
            if vertex not in index:
                strongconnect(vertex)

        return result

g = Graph()

# Example Usage:

# Adding vertices and edges to the graph
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('A', 'D')
# g.add_edge('B', 'E')
# g.add_edge('C', 'F')
# g.add_edge('D', 'G')

# Printing the current state of the graph
# print(g)

# Getting neighbors of vertex 'A'
# g.get_neighbours('A')

# Performing a breadth-first traversal starting from vertex 'A'
# print("BFS traversal:", g.bfs_traversal('A'))

# Counting nodes at level 2 starting from an arbitrary vertex (e.g., the first vertex)
# print(g.count_of_nodes(2))

# Adding vertices and edges for a different graph
# g.add_edge(0, 8)
# g.add_edge(0, 3)
# g.add_edge(0, 1)
# g.add_edge(1, 7)
# g.add_edge(7, 2)
# g.add_edge(2, 5)
# g.add_edge(2, 3)
# g.add_edge(5, 6)
# g.add_edge(3, 4)
# g.add_edge(4, 8)

# Performing a depth-first traversal starting from vertex 5
# print("DFS traversal:", g.dfs_traversal(5))

#Creating components to handle separate components or connected graph
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(3, 4)
# g.traverse_components_if_exist()

# Finding the shortest path between 'A' and 'D' 
# g.add_edge('A', 'B')
# g.add_edge('B', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'D')
# print(g.find_shortest_path('A', 'D'))

# Finding all possible paths between 'A' and 'C'
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'C')
# g.add_edge('B', 'D')
# g.add_edge('D', 'C')
# print(g.all_possible_paths('A', 'C'))

# Test the graph for cycles
# g.add_edge('A', 'B')
# g.add_edge('B', 'C')
# g.add_edge('B', 'K')
# g.add_edge('C', 'A')
# print(g.has_cycle())

# Check for cycles in the directed graph
#Comment these two lines in the "add_edge" method to make "has_cycle_directed" method work correctly
# if vertex1 not in self.graph[vertex2]:
#     self.graph[vertex2].append(vertex1)
# g.add_edge('A', 'B')
# g.add_edge('B', 'C')
# g.add_edge('C', 'A')
# print(g.has_cycle_directed())

# Obtaining the topological order of subjects or tasks based on dependencies.
# g.add_edge('Math', 'Physics')
# g.add_edge('Math', 'Biology')
# g.add_edge('Physics', 'Chemistry')
# g.add_vertex('Art') 
# print(g.topological_sort())

# Performs topological sort for directed graph with Khan's algorithm
#Comment these two lines in the "add_edge" method to make "khans_algorithm_directed" method work correctly
# if vertex1 not in self.graph[vertex2]:
#     self.graph[vertex2].append(vertex1)
# g.add_edge('A', 'B')
# g.add_edge('A', 'C')
# g.add_edge('B', 'D')
# g.add_edge('C', 'D')
# g.add_edge('D', 'E')
# print(g.khans_algorithm_directed())

# Find strongly connected components using Kosaraju's algorithm
#Comment these two lines in the "add_edge" method to make "kosaraju_algorithm" method work correctly
# if vertex1 not in self.graph[vertex2]:
#     self.graph[vertex2].append(vertex1)
# g.add_edge(0, 1)
# g.add_edge(1, 4)
# g.add_edge(1, 2)
# g.add_edge(1, 6)
# g.add_edge(2, 3)
# g.add_edge(3, 2)
# g.add_edge(3, 4)
# g.add_edge(3, 5)
# g.add_edge(4, 5)
# g.add_edge(5, 4)
# g.add_edge(6, 0)
# g.add_edge(6,2)
# print(g.kosaraju_algorithm())

# Find strongly connected components using Tarjan's algorithm
#Comment these two lines in the "add_edge" method to make "tarjan_algorithm" method work correctly
# if vertex1 not in self.graph[vertex2]:
#     self.graph[vertex2].append(vertex1)
# g.add_edge(0, 1)
# g.add_edge(1, 4)
# g.add_edge(1, 2)
# g.add_edge(1, 6)
# g.add_edge(2, 3)
# g.add_edge(3, 2)
# g.add_edge(3, 4)
# g.add_edge(3, 5)
# g.add_edge(4, 5)
# g.add_edge(5, 4)
# g.add_edge(6, 0)
# g.add_edge(6,2)
# print(g.tarjan_algorithm())