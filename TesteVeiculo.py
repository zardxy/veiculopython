# Testando a classe Veículo 

from Veiculo import Veiculo

meuCarroDahora = Veiculo('Onix', '120', 'Branco', 0)

# Exibindo o meu carro dahora
print('\n\t\t\t -- Meu Carro Dahora -- \n')
print(meuCarroDahora)

# Acelerando meu carro dahora
for i in range(0,200):
    meuCarroDahora.acelerar()
    # print(i)

# Exibindo meu carro dahora acelerado
print('\n\t\t\t -- Meu Carro Dahora Acelerado --\n')
print(meuCarroDahora)

# Freando meu carro dahora
for i in range(0,200):
    meuCarroDahora.frear()

# Exibindo o meu carro dahora freado
# print('\n\t\t\t -- Meu Carro Dahora Freado --\n')
# print(meuCarroDahora)