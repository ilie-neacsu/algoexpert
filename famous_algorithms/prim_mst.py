import unittest
import heapq

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

def prim_mst(graph_edges, start=0):

    n = len(graph_edges)
    visited = [False] * n
    mst = [[] for _ in range(n)]
    min_heap = [(0, start, -1)] # (weight, current, previous)

    while min_heap:
        weight, u, prev = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        if prev != -1:
            mst[prev].append([u, weight])
            mst[u].append([prev, weight])

        for v, w in graph_edges[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst

class TestAlgo(unittest.TestCase):
    def test_case_1(self):
        actual = prim_mst(input)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    print(f"input={input}")
    mst = prim_mst(input)
    print(f"mst={mst}")