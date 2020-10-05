def comprimento(lista):
    print(lista)
    c = 0    
    for i in lista:
        c +=1
    return c
def inverte(lista):   
    print(lista[::-1])
def menor(l2):
    p =0
    mnr =l2[p]
    for val in l2:
        if mnr > val:
            mnr = int(val)
    print(f'{mnr}')    
def maior(l2):
    p =0
    mx =l2[p]
    for val in l2:
        if mx < val:
            mx = int(val)
    print(f'{mx}') 
def soma(l2):
    sm = 0
    for num in l2:
        sm+= num
    print(f'{sm}')
def main():
    lista =[]
    while True:
        n = int(input())
        lista.append(n)
        if n == 0:
            lista.pop()
            break
    c = comprimento(lista)
    print(f'{c}')
    inverte(lista)
    menor(lista)
    maior(lista)
    soma(lista)

if __name__=='__main__':
    main()
