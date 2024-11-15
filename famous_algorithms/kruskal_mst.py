import unittest

# input graph given as an adjacency list with [node, weight]
input = [
    [[1, 3], [2, 5]],
    [[0, 3], [2, 10], [3, 12]],
    [[0, 5], [1, 10]],
    [[1, 12]]
]

# output representing the minimum spanning tree given as an adjacency list with elements as [node, weight]
expected = [
    [[1, 3], [2, 5]],
    [[0, 3], [3, 12]],
    [[0, 5]],
    [[1, 12]]
]

def kruskal_mst(graphs_edges):

    sorted_edges = []

    for u, edges in enumerate(graphs_edges):
        for v, w in edges:
            if v > u:
                sorted_edges.append((u, v, w))

    sorted_edges.sort(key=lambda x: x[2])

    n = len(graphs_edges)
    parents = {i: i for i in range(n)}
    rank = [0 for _ in range(n)]
    mst = [[] for _ in range(n)]

    for u, v, w in sorted_edges:
        u_root = find(u, parents)
        v_root = find(v, parents)
        if u_root != v_root:
            mst[u].append([v, w])
            mst[v].append([u, w])
            union(u, v, parents, rank)

    return mst

def find(node, parents):
    if parents[node] != node:
        parents[node] = find(parents[node], parents) # path compression
    return parents[node]

def union(u, v, parents, rank):
    u_root = find(u, parents)
    v_root = find(v, parents)

    if rank[u_root] < rank[v_root]:
        parents[u_root] = v_root
    elif rank[u_root] > rank[v_root]:
        parents[v_root] = u_root
    else: # rank[u_root] == rank[v_root]
        parents[u_root] = v_root
        rank[v_root] += 1

# class TestAlgo(unittest.TestCase):
#     def test_case_1(self):
#         actual = kruskal_mst(input)
#         self.assertEqual(actual, expected)

if __name__ == "__main__":
    mst = kruskal_mst(input)
    print(f"mst={mst}")