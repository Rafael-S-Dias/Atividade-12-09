from models.endereco import Endereco
from models.enum.genero import Genero
from models.enum.setor import Setor
from models.funcionario import Funcionario

class Motoboy(Funcionario):
    BONIFICACAO = 0.10
    
    def __init__(self, nome: str, telefone: str, email: str, cpf: str, rg: str, dataNascimento: str, genero: Genero, matricula: str, setor: Setor, salario: float, endereco: Endereco, cnh: str) -> None:
        super().__init__(nome, telefone, email, cpf, rg, dataNascimento, genero, matricula, setor, salario, endereco)
        self.cnh = cnh

    def salario_final(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        resultado += self.salario
        return resultado

    def __str__(self) -> str:
        return (f"CNH: {self.cnh}\n"
                f"{super().__str__()}"
        ) 