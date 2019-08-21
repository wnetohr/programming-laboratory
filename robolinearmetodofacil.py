comando = input("Digite o comando para o robô linear(f = frente, t = trás): ")
frente = comando.count('f')
tras = comando.count('t')
print('O robô se moveu {} passo(s) da posição inicial'.format(frente - tras))


