import os
from models.juridica import Juridica
from models.enum.genero import Genero
from models.enum.setor import Setor
from models.endereco import Endereco
from models.enum.unidade_federativa import UnidadeFederativa
from models.motoboy import Motoboy
from models.advogado import Advogado
from models.medico import Medico
from models.cliente import Cliente



os.system("cls || clear")

endereco1 = Endereco("Rua ....", 1202, "Apto 02", "41......", "Salvador", UnidadeFederativa.BAHIA)
cliente1 = Cliente("Rosilene", "71988", "Rosilene..", "Rosilene@..", "5579548982", "28/05/1969", Genero.FEMININO, endereco1, "55555" )
advogado1 = Advogado("Rafael", "71988", "Rafael@..", "868582689-48", "164916498", "02/08/2001",Genero.MASCULINO, "444444", Setor.JURIDICO, 5000, endereco1, "8888")
motoboy1 = Motoboy("Luan", "71997", "Luan@..", "478924869-59", "2552659", "23/05/1989", Genero.MASCULINO, "66666", Setor.OPERACOES, 2000, endereco1, "77777" ) 
medico1 = Medico("Juvenal", "71999", "Juvenal@..", "649461779-56", "6416238", "03/05/1967", Genero.MASCULINO, "88888", Setor.SAUDE, 7500, endereco1, "44444")
                   
print(cliente1)
print(motoboy1)
print(advogado1)
print(medico1)
