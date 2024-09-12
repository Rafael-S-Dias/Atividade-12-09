from abc import ABC
from models.pessoa import Pessoa
from models.enum.genero import Genero
from models.endereco import Endereco

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, rg: str, dataNascimento: str, genero: Genero, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.dataNascimento = dataNascimento
        self.genero = genero

    def __str__(self) -> str:
        return (f"CPF: {self.cpf}\n"
                f"RG: {self.rg}\n"
                f"Data de Nascimento: {self.dataNascimento}\n"
                f"Genero: {self.genero.value}\n"
                f"{super().__str__()}"
        )