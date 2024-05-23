import sys
input = sys.stdin.readline 

n = int(input())
graph = {}
parent = {}
for i in range(n):
    p, c1, c2 = map(str, input().split())
    graph[p] = [c1, c2]



def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(graph[root][0])
        preorder(graph[root][1])
        


def inorder(root):
    if root != '.':
        inorder(graph[root][0])
        print(root, end ='')
        inorder(graph[root][1])
    
        
def postorder(root):
    if root != '.':
        postorder(graph[root][0])
        postorder(graph[root][1])
        print(root, end ='')
        
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
    