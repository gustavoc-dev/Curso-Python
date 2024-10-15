maiorIdade = 0
homens = 0
mulheresMenosVinte = 0
cont=1
while cont==1:
    age = int(input('Qual é a idade dessa pessoa?\n'))
    sexo = str(input('Qual é o sexo dessa pessoa? [M/F]\n')).strip().upper()
    if age>=18:
        maiorIdade+=1
    elif age>=18 and sexo=='M':
        maiorIdade+=1
        homens+=1
    elif age <20 and sexo=='F':
        maiorIdade+=1
        mulheresMenosVinte+=1
    cont = int(input('Quer continuar?\n[1]Sim\n[2]Não\n'))
    if cont ==2:
        break
print(f'Foram inseridos {homens} homens, {mulheresMenosVinte} Mulheres com menos de 20 e {maiorIdade} maiores de 18 anos')
