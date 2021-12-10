from random import*
acho=""
senha = input("Digite a senha que deseja quebrar: ")
letras = ['a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z','ç','1','2','3',
        '4','5','6','7','8','9','0','!','@','#',
        '$','%','*','(',')','{','}','^','¨','?']

while(acho != senha):
    acho=""
    for letra in senha:
        acholetra=letras[randint(0,49)]
        acho=str(acholetra) + str(acho)
    print(acho)
print("A senha encontrada foi: {}". format(acho))

