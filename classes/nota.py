class Nota:

    # Construtor
    def __init__(self, nota, disciplina, cargaHoraria):
        self.ListaNota = nota
        self.ListaDisciplina = disciplina
        self.ListaCargaHora = cargaHoraria

    # Método para multiplicar a nota pela carga horaria da disciplina, referente ao calculo de CR.
    def calculaHoraXNota(self):
        return [x*y for x,y in zip(self.ListaNota,self.ListaCargaHora)] # retorna uma lista com o valor da Nota*Carga horaria de cada disciplina.

    # Métodos para configuração de variáveis
    def setNota(self, nota):
        self.ListaNota =  nota

    def setDisciplina(self, disciplina):
        self.ListaDisciplina = disciplina

    def setListaCargaHora(self, cargaHora):
        self.ListaCargaHora = cargaHora

    # Métodos para acesso às variáveis
    def getNota(self):
        return self.ListaNota

    def getListaDisciplina(self):
        return self.ListaDisciplina

    def getListaCargaHora(self):
        return self.ListaCargaHora

