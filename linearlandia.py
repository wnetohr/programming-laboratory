def find_path(graph, start, end, path=[]):                  #função dada pelo professor em sala que acha o caminho
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
alcance, x, y = map(int,input().split())                    #pega o número de cidades, a cidade inicial e o destino final
graph = {}
lista = []
custo = 0                                                      #contador de custo para ir de uma cidade para outra
for n in range(alcance - 1):                                #aqui ele bota os valores no grafo
    gy, ga, dist = map(int,input().split())
    graph[gy] = [ga,dist]
    graph[ga] = [gy,0]
inicio = x
fim = y
a = find_path(graph,inicio,fim)
for n in a:                                                 #esse for é usado para buscar os custos no grafo e adicionarem eles no contador
    if n in graph:
        lista = graph[n]
        custo += lista[1]
print(custo)

