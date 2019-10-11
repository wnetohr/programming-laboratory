#minha ideia é fazer um grafo com o input dado pelo usuário, fazer todas as rotas possivéis e dar print na rota com o menor custo

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)

            if newpath: return newpath
    return None
grafo = {}
n, m = map(int,input().split())
for x in range(m):
    a, b, c = map(int,input().split())
    grafo[x] = [a,b,c]
sublista = grafo[0]
inicio = sublista[0]
fim = n
resultado = find_path(grafo,inicio,fim)
print(resultado)

#n consegui implementar a tempo o dijkstra para achar o caminho mais curto, pensei em fazer com o findpath e depois mostrar a que tivesse o menor custo
#porém o findpath apenas acha um caminho, é nescessário implementar o dijkstra.