from classes.nota import Nota

class Aluno:

    # Construtor
    def __init__(self, matricula, nota, somaHora):
        self.codMatricula = matricula
        self.Notas = nota
        self.totalHoras = somaHora
        self.cr = 0

    def calculoCR(self):
        # Pega a lista de Nota*Hora contendo todas as notas do aluno multiplicadas pelas suas respectivas cargas horarias e soma a lista em um inteiro.
        # Após, divide pelo número total de horas e é arredondado.
        self.cr = round(sum(self.Notas.calculaHoraXNota())/self.totalHoras)
        return self.cr # retorna o CR.

    

    # Métodos para configuração de variáveis
    def setCr(self,cr):
        self.cr = cr

    def setMatricula(self, matricula):
        self.codMatricula = matricula

    # Métodos para acesso às variáveis
    def getCr(self):
        return self.cr

    def getMatricula(self):
        return self.codMatricula

