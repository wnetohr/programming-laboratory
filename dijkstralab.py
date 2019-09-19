#esse código já possui um grafo pronto e o usuário escolhe um ponto inicial
#e um final para ele mostrar o caminho mais curto
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

if __name__ == "__main__":
    grafo = {'a': {'b': 4, 'c': 6, 'f': 5},
            'b': {'d': 7, 'e': 6, 'f':4},
            'c': {'h': 5, 'i': 9, 'g': 4},
            'd': {'e': 5, 'j': 8},
            'e': {'f': 6, 'j': 9, 'd': 5},
            'f': {'e': 6, 'j': 10, 'i': 5, 'h': 4},
            'g': {'i': 10},
            'h': {'f': 4, 'j': 12, 'i': 5},
            'i': {'f': 5, 'j': 8},
            'j': {'d': 8, 'e': 9, 'f': 10, 'h': 12, 'i': 8}}
    print(grafo)
    p_inicial = input("Digite o ponto inicial: ")
    p_final = input("Digite o ponto final: ")
    dijkstra(grafo,p_inicial,p_final)
