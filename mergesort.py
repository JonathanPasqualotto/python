import os
os.system('clear')

contador = 0
def mergeSort(alist):
    global contador
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            contador +=1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            contador +=1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            contador +=1
            k=k+1
    print("Merging ",alist)


while True:
    vetor = list(map(int,input().split()))
   # print(vetor.sort())
   # print(len(vetor))
    if vetor == 0:
        break
    vet = mergeSort(vetor)
    print(vet)
    print(contador)
    if (contador % 2) == 0:
        print ('Carlos')
        contador = 0
    else:
        print ('Marcelo')
        contador = 0

