






arq = open('tt.txt', 'r')
# arq.readline

for linha in arq:

    print(arq.readline().rstrip(), arq.readline().rstrip(), arq.readline())