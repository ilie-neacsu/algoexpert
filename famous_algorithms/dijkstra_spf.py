import heapq
import unittest

# input:
# start_node: start node
# graph_edges: graph given as an adjacency list containing elements like [node, weight]
start_node = 0
graph_edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    [],
]

# output:
#   distances[i] = minimum distance between start and i
#   distances[start_node] = 0
#   distances[i] = -1 if start and i are not connected
distances = [0, 7, 13, 27, 10, -1]

def dijkstra_spf(start_node, graph_edges):

    distances = [float("inf") for _ in range(len(graph_edges))]
    distances[start_node] = 0
    priority_queue = [(0, start_node)] # (distance, node)

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distances[node]:
            continue

        for neighbor, weight in graph_edges[node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return [-1 if distance == float("inf") else distance for distance in distances]

class AlgoTest(unittest.TestCase):

    def test_case_1(self):
        expected = dijkstra_spf(start_node, graph_edges)
        self.assertEqual(distances, expected)


if __name__ == "__main__":
    distances = dijkstra_spf(start_node, graph_edges)
    print(distances)