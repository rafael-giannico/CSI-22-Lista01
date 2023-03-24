
soma = 0

def sum_to(n):
    global soma
    if n == 1:
        soma += 1
    else:
        soma += n
        sum_to(n-1)

sum_to(10)
print(soma)
