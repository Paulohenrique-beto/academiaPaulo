# 1) Faça um programa que receba quatro número e mostre a media entre os quatro 
# Dica: media = (n1+n2+n3+n4)/4 
# usar input()

# def media():
#     numero1 = int(input("Digite o primeiro número"))
#     numero2 = int(input("Digite o segundo número"))
#     numero3 = int(input("Digite o terceiro número"))
#     numero4 = int(input("Digite o quarto número"))
#     media = (numero1+numero2+numero3+numero4)/4
#     return media 

# print(media())

# 2) Faça um programa que receba dois inputs, uma palavra/frase e uma letra.
#  O programa deve retornar quantas vezes a letra apareceu na palavra/frase. Dica: contagem de valores .count('valor")

# def pesquisa():
#     letra = str(input("Digite a letra para ser pesquisada: "))
#     frase = str(input("Digite a frase para que a pesquisa aconteça : "))
#     pesquisa = int(frase.count(letra))
#     return pesquisa

# print(pesquisa())

# 3) Faça um programa que receba quantos números terá no cálculo da média e retorne a média deles.
# 	Exemplo: "Quantos números: 10"  --> (n1+n2+...+n10)/10
# 	Dica: podemos usar estruturas de repetição... tipo o for... e definir o range... 

# numero = float(input("Digite seu numero: "))
# i = 0
# soma = 0
# while i < numero:
#     # print(i)
#     soma += i
#     i += 1
#     if i == numero:
#         print(soma/numero)


# 4) Faça um programa que receba dois números e mostre:
# -A soma
# -A subtração
# -A multiplicação
# -E a divisão entre os dois

# P.S.: função 'input()' receba valores no tipo string! para alterar: int() e float()

# num1 = float(input("Digite o primeiro numero : "))
# num2 = float(input("Digite o segundo numero : "))
# subtração = num1-num2
# multiplicação = num1*num2
# divisao = num1/num2
# print("Sua subtraçao foi {} a multiplicaçao {} e a divisao {}".format(subtração,multiplicação,divisao))


# Calculadora

#n1 = float(input("Insira o 1 numero:"))
#n2 = float(input("Insira o 2 numero: "))

#class Calculadora:
    


#    def soma(self,n1,n2):
        
#        result = n1 + n2
#        return result

#    def subtracao(self,n1,n2):
#        result = n1 - n2
#        return result
    
#    def divisao(self,n1,n2):
#        result = n1 / n2
#        return result

#    def multiplicacao(self,n1,n2):
#        result = n1 * n2
#        return result

#escolha = str(input("Selecione uma das opcoes abaixo: " + "\n" +"1 - adição\n" +"2- Subtração\n" + "3- Divisao\n" + "4- Multiplicação\n"))

#calculadora = Calculadora()
#if(escolha == 1):
#    print("O resultado e: " ,calculadora.soma(n1,n2))
#elif(escolha == 2):
#    print("O resultado e: " ,calculadora.subtracao(n1,n2))
#elif(escolha == 3):
#    print("O resultado e: " ,calculadora.divisao(n1,n2))
#elif(escolha == 4):
#    print("O resultado e: " ,calculadora.mutiplicacao(n1,n2))



# 5) Escreva um programa que leia o nome de um funcionário, seu número de horas trabalhadas,
#  o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o nome e o salário do funcionário.

# def leia():
#     nome = str(input("Digite o nome do funcionário : "))
#     valor = float(input("Digite o valor que recebe por hora : "))
#     horas = float(input("Digite quantas horas foram trabalhadas:  "))
#     salario = float(horas*valor)
#     return ("{} você trabalhou {} horas neste mês , sendo assim seu sálario será de {}" . format(nome,horas,salario))
# print(leia())


# 6) Criar as respectivas Classes:

# -Pessoa
# -Pet

# -Modelar atributos no __init__
# -criar métodos na classe Pessoa:
# -Retornar Nome da Pessoa
# - Retornar idade da Pessoa

# -criar métodos na classe pet:
# -Retornar nome de pet e nome do seu dono
# -retornar todas as infos do pet

# Testar todos os métodos criados printando em tela os resultados solicitados acima

 nomed = input("Informações Dono"+"\n"+"Informe seu nome: ")
 idaded = input("Informe sua idade: ")
 print("\n")
 nomep = input("Informações PET"+"\n"+"Informe o nome: ")
 idadep = input("Informe a idade: ")
 print("\n")
 class Pessoa():

     def __init__(self,nome,idade):
         self.nome = nomed
         self.idade = idaded

      def pessoa(self):
          return
       
        
 class Pet():

     def __init__(self,nome,idade,dono):
         self.nome = nomep
         self.idade = idadep
         self.dono = dono
        
      def idade_pet(self):
          aux = int(input("Insira o ano de nascimento do seu Pet:"))
          idade = 2019 - aux
          return idade
       
        
        
 pessoas = Pessoa(nomed,idaded)
 pets = Pet(nomep,idadep,pessoas.nome)

 print("Dono:","\n","Nome: " , pessoas.nome ,"\n","Idade: " , pessoas.idade )
 print("\n")
 print("PET","\n","Nome:" , pets.nome,"\n", "Idade: ", pets.idade,"\n","Dono: ",pets.dono) 


## UM POUCO DE REDES 

    ## Computadores compartilhando recursos
    ## Metodo de requisição HTTP anda junto com os status, metodo post pega dados, atualização dos dados pode ser o put, metodo delete http
    ## URL pode trazer diferentes resultados, diferentes resultados com diferentes metodos
    ## IP endereço de identificador unico de cada maquina (endereço da maquina, pra onde devovler)
    ## DNS nome do servidor, onde faz a requisição e ele pega o site e devolve pro IP
    ## CRUD cada letra tem uma função especifica, C --> Create --> Criar coisas no banco, R --> Read --> Consultar o banco, U --> Update --> associado ao input do HTTP e D --> Delete --> deleta
    ## API é um conector que faz a ligação entre sistemas diferentes, end points para fazer consultar inserções e outras coisas, ele determina os dados pelos metodos HTTP, 
    ##a função conecta coisas diferentes e faz os sistemas serem interligados.