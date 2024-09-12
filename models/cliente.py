from models.endereco import Endereco
from models.enum.genero import Genero
from models.fisica import Fisica


class Cliente(Fisica):
   def __init__(self, nome: str, telefone: str, email: str, cpf: str, rg: str, dataNascimento: str, genero: Genero, endereco: Endereco, protocoloAtendimento: str ) -> None:
      super().__init__(nome, telefone, email, cpf, rg, dataNascimento, genero, endereco)
      self.protocoloAtendimento = protocoloAtendimento

   def __str__(self) -> str:
       return (f"Protocolo de Atendimento: {self.protocoloAtendimento}\n"
               f"{super().__str__()}"
       )

                