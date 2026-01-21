# Escopo global é o escopo onde todo código é alncançável.
# Escopo local é o escopo onde o código só é alcançável dentro de uma função ou bloco.

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

escopo()
print(x)