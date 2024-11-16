import heapq
from turtledemo.penrose import start

# input

start_node = 0
end_node = 6
graph_edges = [
    [[1, 7]],
    [[2, 6], [3, 20], [4, 3]],
    [[3, 14]],
    [[4, 2]],
    [],
    [],
]

# output
path = [0, 1, 4]
distance = 10 # 7 + 3


def dijkstra_path(start_node, end_node, graph_edges):

    path = []
    come_from = {}
    distances = [float("inf") for _ in range(len(graph_edges))]
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distances[node]:
            continue

        if node == end_node:
            path_node = end_node
            while path_node != start_node:
                path.append(path_node)
                path_node = come_from[path_node]
            path.append(start_node)
            return list(reversed(path)), distances[end_node]

        for neighbor, weight in graph_edges[node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                come_from[neighbor] = node
                heapq.heappush(priority_queue, (distance, neighbor))

    return [], -1

if __name__ == "__main__":
    path = dijkstra_path(start_node, end_node, graph_edges)
    print(path)