print()
print("Digite um CPF para verificar se ele se configura como válido")
cpf9 = input("Insira os primeiros 9 números do CPF: ")
cpf2 = input("Insira os dígitos de controle(os dois últimos números do CPF): ")
print()

if (len(cpf9) == 9) and (len(cpf2) == 2):
    
    cpf9listint = []
    for x in cpf9:
        cpf9listint.append(int(x))
        
    cpf2listint = []
    for y in cpf2:
        cpf2listint.append(int(y))
    
    b = 0
    for i in range(9):
        a = cpf9listint[i] * (10 - i)
        b = b + a
    
    c = b % 11
    
    if c >= 2:
        pdc = 11 - c
        
    elif c == 1 or c == 0:
        pdc = 0
        
    e = 0
    cpf9listint.append(pdc)
    
    for t in range(10):
        d = cpf9listint[t] * (11 - t)
        e = e + d
    
    f = e % 11
    
    if f >= 2:
        sdc = 11 - f
        
    elif f == 1 or f == 0:
        sdc = 0
    
    if cpf2listint[0] == pdc and cpf2listint[1] == sdc:
        print("CPF válido")
        print(cpf9 + cpf2)
    else:
        print("CPF inválido")
        print(cpf9 + cpf2)
