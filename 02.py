def conta(l, el):
    t=0

    for p in range(len(l)):
        if l[p]==el:
            t+=1
    print(f'{t}')

def main():
    l=[]
    while True:
        n = int(input())
        l.append(n)
        if n ==0:
            l.pop()
            break
    el = int(input())
    print(l)
    print(el)   

    conta(l, el)
if __name__=='__main__':
    main()
