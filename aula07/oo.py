class Mamiferos():
  olhos = 2
  patas = 4

# metodo construtor / self-> propria  instancia do objeto->se refere a ele mesmo == this do java
  def __init__(self,pelo,especie,rabo,cor):

    self.pelo = pelo
    self.especie = especie
    self.rabo = rabo
    self.cor = cor

  def comer(self):
    print("Comi")
  def fazer_som(self):
    print("Aaaaaa")
  def dormir(self):
    print("Dormi")

  

  #criar instancia  / instanciar um objeto
mamifero = Mamiferos("curto","doguinhos caninos" ,True , "caramelo")

mamifero2 = Mamiferos("longo","agrarios monata" ,False , "purple")

mamifero.comer()
mamifero2.fazer_som()
print(mamifero.especie)
print(mamifero2.especie)

# exemplo de herança
#parametro = classe pai
class Gato(Mamiferos):
      # todos os atributos da classe pai + os atributos da propria classe
      def __init__(self,pelo,especie,rabo,cor,bigodes):
            #inicializa | herda os atributos da classe pai = super, e inicializa __init__
            super().__init__(pelo,especie,rabo,cor)
            self.bigodes = bigodes
      
      def fazer_som(self):
            print("Miauuuuuuuuuuuuuuu")

gatinho = Gato("super curto","peladus egiptum",True,"bege organico",5)
print(gatinho.especie)
print(gatinho.bigodes)
gatinho.fazer_som()
gatinho.comer()
            
