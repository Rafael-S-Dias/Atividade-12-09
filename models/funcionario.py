from abc import ABC, abstractmethod
from models.endereco import Endereco
from models.enum.genero import Genero
from models.fisica import Fisica
from models.enum.setor import Setor

class Funcionario(Fisica, ABC):
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, rg: str, dataNascimento: str, genero: Genero, matricula: str, setor: Setor, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, cpf, rg, dataNascimento, genero, endereco)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"Numero de Matricula: {self.matricula}\n"
                f"Setor: {self.setor.value}\n"
                f"Salario: {self.salario}\n"
                f"Salario Final: {self.salario_final()}\n"
                f"{super().__str__()}"
        )