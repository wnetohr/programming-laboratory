def dfs(grafo,inicial,final,caminho=[]):
    caminho = caminho + [inicial]
    if inicial==final:
        return caminho
    for k in grafo[inicial-1]:
        if k not in caminho:
            rec = dfs(grafo,k,final,caminho)
            if rec: return rec
    return None


n, a, b = map(int, input().split())
grafo = [[] for x in range(n)]
for x in range(n-1):
    p, q = map(int, input().split())
    grafo[p-1] = grafo[p-1]+[q]
    grafo[q-1] = grafo[q-1]+[p]
#print(grafo)
print(len(dfs(grafo,a,b))-1)