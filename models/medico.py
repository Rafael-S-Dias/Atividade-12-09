from models.endereco import Endereco
from models.enum.genero import Genero
from models.enum.setor import Setor
from models.funcionario import Funcionario

class Medico(Funcionario):
    BONIFICACAO = 0.50

    def __init__(self, nome: str, telefone: str, email: str, cpf: str, rg: str, dataNascimento: str, genero: Genero, matricula: str, setor: Setor, salario: float, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, cpf, rg, dataNascimento, genero, matricula, setor, salario, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        resultado += self.salario
        return resultado

    def __str__(self) -> str:
        return (f"CRM: {self.crm}\n"
               f"{super().__str__()}"
        ) 