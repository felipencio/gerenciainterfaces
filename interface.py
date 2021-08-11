class Interface:
 def _init_(self,nome,ip):
    self.nome = nome
    self.ip=ip
    
 def update(self,nome,ip):
        self.nome = nome
        self.ip=ip
 def imprime(self):
    print(self.nome + ":" +self.ip)
    