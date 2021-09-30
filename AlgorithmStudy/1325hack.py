import sys
from collections import deque
sys.stdin = open("AlgorithmStudy/1325.txt", 'r')


def main():
    global relation_graph, relation, computers
    computers, relation = map(int, sys.stdin.readline().split())
    relation_graph = get_relation(computers)
    max_hack = 0
    result = []
    for i in range(1, relation+1):
        if relation_graph[i]:
            candidate = bfs(i)
            if candidate >= max_hack:
                if candidate > max_hack:
                    result = []
                max_hack = candidate
                result.append(i)
    print(*result)


def get_relation(computers):
    relation_graph = [[] for _ in range(computers+1)]
    for _ in range(relation):
        receiver, giver = map(int, sys.stdin.readline().split())
        relation_graph[giver].append(receiver)
    return relation_graph


def bfs(start):
    hacked = 0
    queue = deque()
    queue.append(start)
    visited = [False] * (computers+1)
    visited[start] = True
    while queue:
        now = queue.popleft()
        hacked += 1
        for next in relation_graph[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
    return hacked



if __name__ == "__main__":
	main()