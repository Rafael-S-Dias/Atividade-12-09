from abc import ABC
from models.pessoa import Pessoa
from models.endereco import Endereco

class Juridica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, cnpj: str, inscricaoEstadual: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return (f"CNPJ: {self.cnpj}\n"
                f"Inscrição Estadual: {self.inscricaoEstadual}\n"
                f"{super().__str__()}"
        )