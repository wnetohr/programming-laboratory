def dijkstra(grafo,xdt,destino,passou=[],distancia={},anterior={}):
    if xdt == destino:
        caminho=[]
        ant=destino
        while ant != None:
            caminho.append(ant)
            ant=anterior.get(ant,None)
        print('caminho mais curto: '+str(caminho)+" distancia = "+str(distancia[destino]))
    else :
        if not passou:
            distancia[xdt]=0
        for vizinho in grafo[xdt] :
            if vizinho not in passou:
                nova_distancia = distancia[xdt] + grafo[xdt][vizinho]
                if nova_distancia < distancia.get(vizinho,float('inf')):
                    distancia[vizinho] = nova_distancia
                    anterior[vizinho] = xdt
        passou.append(xdt)
        naopassou={}
        for k in grafo:
            if k not in passou:
                naopassou[k] = distancia.get(k,float('inf'))
        x=min(naopassou, key=naopassou.get)
        dijkstra(grafo,x,destino,passou,distancia,anterior)

n, m = map(int,input().split())
grafo = {x + 1: {} for x in range(n)}
for j in range(m):
    a, b, c = map(int,input().split())
    grafo[a].update(dict({b: c}))
    grafo[b].update(dict({a: c}))
resultado = dijkstra(grafo,1,n)
print(resultado)
