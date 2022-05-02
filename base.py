from manipulaDados import *

# Carrega a lista de objetos alunos
listaAluno = carregaAlunos()

# Carrega a lista de objetos curso
listaCursos = carregaCursos()

# Calcula o CR dos alunos, exibe no terminal o resultado como no exemplo e retorna uma lista de CR e Matriculas que possuem index equivalentes.
Matriculas, CRs = CalculoCR(listaAluno)

# Calcula a média de CR dos cursos, exibe no terminal o resultado como no exemplo e retorna uma lista de Código e CR de cursos que possuem index equivalentes.
CodCursos, CRCursos = mediaCRCurso(listaCursos, Matriculas, CRs)

# Cria uma lista de tuplas para ser utilizada na GUI
GUIACursos = list(zip(CodCursos, CRCursos))

GUIAlunos = list(zip(Matriculas,CRs))