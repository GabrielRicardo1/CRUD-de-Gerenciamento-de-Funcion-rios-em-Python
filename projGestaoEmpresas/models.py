class Funcionario:
    def __init__(self, nome, cargo, salario, cpf, data_contratacao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.cpf = cpf
        self.data_contratacao = data_contratacao

    def __str__(self):
        return (
            f"Nome: {self.nome}, Cargo: {self.cargo}, "
            f"Salário: R${self.salario:.2f}, CPF: {self.cpf}, "
            f"Data de Contratação: {self.data_contratacao}"
        )


class SistemaCadastro:
    def __init__(self):
        self.funcionarios = []
