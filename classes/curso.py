class Curso:

    # Construtor
    def __init__(self, curso, alunos):
        self.codCurso = curso
        self.listaAlunos = alunos

    # Métodos para configuração de variáveis
    def setListaAlunos(self, alunos):
        self.listaAluno = alunos
    
    def setCodCurso(self, curso):
        self.codCurso = curso

    # Métodos para acesso às variáveis
    def getListaAlunos(self):
        return self.listaAlunos
    
    def getCodCurso(self):
        return self.codCurso



