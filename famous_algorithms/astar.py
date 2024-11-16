import heapq
import unittest
import copy

# input
start_node = (0, 1)
end_node = (4, 3)

graph = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 0, 0, 0, 0],
]

# output
shortest_path = [(0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3)]
distance = 8

# [
# [., ., 0, 0, 0],
# [., 1, 1, 1, 0],
# [., ., 0, 0, 0],
# [1, ., 1, 1, 1],
# [0, ., ., ., 0],
# ]

def astar(start_node, end_node, graph):

  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  rows, cols = len(graph), len(graph[0])

  come_from = {}
  g_score = {start_node: 0}
  f_score = {start_node: heuristic(start_node, end_node)}
  priority_queue = [(0, start_node)]

  while priority_queue:

    _current_f_score, current_node = heapq.heappop(priority_queue)

    if current_node == end_node:
      path = []
      path_node = end_node
      while path_node != start_node:
        path.append(path_node)
        path_node = come_from[path_node]
      path.append(start_node)
      return list(reversed(path)), g_score[end_node]

    for neighbor in neighbors(current_node, directions, rows, cols):
      tentative_g_score = g_score[current_node] + 1
      if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
        come_from[neighbor] = current_node
        g_score[neighbor] = tentative_g_score
        f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end_node)
        heapq.heappush(priority_queue, (f_score[neighbor], neighbor))

  return None, -1

def heuristic(node, goal):
  return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def neighbors(node, directions, rows, cols):
  node_neighbors = []
  for direction in directions:
    neighbor = (node[0] + direction[0], node[1] + direction[1])
    in_grid = (0 <= neighbor[0] < rows) and (0 <= neighbor[1] < cols)
    if in_grid and graph[neighbor[0]][neighbor[1]] == 0:
      node_neighbors.append(neighbor)
  return node_neighbors

def draw_path(path, graph):
    graph_copy = copy.copy(graph)
    for x, y in path:
      graph_copy[x][y] = '-'

    result = []
    for row in graph_copy:
      result.append('\t[' + ', '.join(map(str, row)) + ']')

    return '[\n' + ',\n'.join(result) + '\n]'

class TestAlgo(unittest.TestCase):
  def test_case_1(self):
    expected_path, expected_distance = astar(start_node, end_node, graph)
    self.assertEqual(expected_path, shortest_path)
    self.assertEqual(expected_distance, distance)

if __name__ == "__main__":
  path, distance = astar(start_node, end_node, graph)
  print(f"path={path}")
  print(f"distance={distance}")
  print(draw_path(path, graph))