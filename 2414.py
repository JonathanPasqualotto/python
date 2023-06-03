while True:
    vet = list(map(int, input().split()))
    if 0 in vet:
        break
    
print(max(vet))