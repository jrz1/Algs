class PathFinder(object):

    def __init__(self, points):
        self.graph  = self._construct_adjacency_list(points)
        self._cache = {}

    def _construct_adjacency_list(self, points):
        graph = {}
        for p in points:
            less, more = min(p), max(p)

            if less not in graph:
                graph[less] = set([more])
            else:
                graph[less].add(more)
        return graph

    def dfs(self, start):

        """
            Standard DFS with 0(|V| + |E|) Time
            and O(V) auxiliary space
        """

        visited = set()
        stack = [start]

        _count = 0
        while stack:
            _count += 1
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                if vertex in self.graph:
                    stack.extend(v for v in self.graph[vertex])

        print "Start: {s} | Count: {c} |".format(c=_count, s=start),
        return visited

    def dfs_cache(self, start):

        """
            Modified DFS to cache previous 
            paths at expense of increased space
            0(|V| + |E|) Time (although practically faster,
            depending on the given data set), but with O(V^2)
            auxiliary space
        """

        visited = set()
        stack = [start]

        _count = 0
        while stack:
            _count += 1
            
            vertex = stack.pop()
            if vertex not in visited:
                if vertex in self._cache:
                    visited.update(self._cache[vertex])
                else:
                    visited.add(vertex)
                    if vertex in self.graph:
                        stack.extend([v for v in self.graph[vertex]])
        self._cache[start] = visited

        print "Start: {s} | Count: {c} |".format(c=_count, s=start),
        return visited

def main():

    points = set([
        (16, 17),
        (15, 16),
        (14, 15),
        (11, 14),
        (12, 13),
        (10, 12),
        (11, 9),
        (10, 9), 
        (9, 6), 
        (6, 2), 
        (8, 5), 
        (5, 4), 
        (4, 2), 
        (2, 1), 
        (3, 1),
        (7, 3),
    ])

    p = PathFinder(points)
    
    print "---- Cached ----"
    print p.dfs_cache(1)
    print p.dfs_cache(2)
    print p.dfs_cache(9)
    print p.dfs_cache(6)
    print p.dfs_cache(2)

    print "\n---- Standard ----"
    print p.dfs(1)
    print p.dfs(2)
    print p.dfs(9)
    print p.dfs(6)
    print p.dfs(2)

if __name__ == '__main__':
    main()
