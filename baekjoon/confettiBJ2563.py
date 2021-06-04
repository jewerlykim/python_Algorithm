import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/confetti.txt", 'r')
input = sys.stdin.readline
n = int(input())

graph_set = set()

def paste_confetti(x,y):
    for i in range(10):
        for j in range(10):
            graph_set.add((x+i, y+j))



for _ in range(n):
    x, y = map(int, input().split())
    paste_confetti(x,y)


print(len(graph_set))