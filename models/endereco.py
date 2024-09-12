from models.enum.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf : UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade
        self.uf = uf

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}\n"
                f"Numero: {self.numero}\n"
                f"Complemento: {self.complemento}\n"
                f"CEP: {self.cep}\n"
                f"Cidade: {self.cidade}\n"
                f"UF: {self.uf.nome} / {self.uf.sigla}\n"
        )