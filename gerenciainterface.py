import interface

if __name__ == "__main__":
	descricao = input("Descricao do Equipamento:")
	nInt = int(input("Quantas interfaces:"))
	n=1
	interfaces=[]
	while (n<=nInt):
		nome=input("Qual nome da Interface:")
		ip=input("Qual IP da Interface:")
		novaInterface = interface.Interface(nome,ip)
		interfaces.append(novaInterface)
		n=n+1
		
	print("--- RELATORIO ---")
	print("Equipamento: " + descricao) 
	
	for inter in interfaces:
		inter.imprime()