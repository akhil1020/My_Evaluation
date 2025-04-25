import heapq

def dijkstra(graph, start, destination):
    heap = [(0, start, [start])]
    visited = set()

    while heap:
        distance, current, path = heapq.heappop(heap)
        
        if current == destination:
            print(f"Shortest path from {start} to {destination}: {' -> '.join(path)}")
            print(f"Total distance: {distance}")
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(heap, (distance + weight, neighbor, path + [neighbor]))

    print(f"No path found from {start} to {destination}.")


cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'


dijkstra(cities, start_city, destination_city)
