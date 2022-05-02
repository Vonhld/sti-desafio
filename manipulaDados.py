import pandas as pd
from classes.aluno import Aluno
from classes.curso import Curso
from classes.nota import Nota

# Carrega o dataset.
dataset = pd.read_csv('dataset/notas.csv')

def carregaAlunos():
	listaAlunos = []
	# Carrega as colunas ['MATRICULA','COD_DISCIPLINA','NOTA','CARGA_HORARIA'], agrupadas pelo código da matrícula.
	alunos = dataset[['MATRICULA','COD_DISCIPLINA','NOTA','CARGA_HORARIA']].groupby('MATRICULA')

	for matricula, aluno in alunos:	# Itera o agrupamento passando por cada aluno.
		somaTotalHoras = aluno.CARGA_HORARIA.sum()	# Guarda a soma de carga horaria do aluno.
		
		listaNotas = aluno.NOTA					# Guarda todas as notas do aluno.
		listaDisciplinas = aluno.COD_DISCIPLINA	# Guarda todas as disciplinas do aluno.
		listaCargaHoraria = aluno.CARGA_HORARIA	# Guarda todas as cargas horarias dos alunos.
		# Importante: O index das 3 listas [listaNotas,listaDisciplinas,listaCargaHoraria] são equivalentes.
		
		# Criação do objeto nota.
		nota = Nota(listaNotas, listaDisciplinas, listaCargaHoraria)

		# Criação do objeto aluno que recebe como parâmetro, o objeto Nota.
		objetoAluno = Aluno(matricula, nota, somaTotalHoras)

		# Add o objetoAluno na lista de alunos.
		listaAlunos.append(objetoAluno)
	
	return listaAlunos	# retorna a lista de objetos aluno.

def carregaCursos():
	listaCursos = []
	# Carrega as colunas ['COD_CURSO','MATRICULA'], agrupadas pelo código do Curso.
	cursos = dataset[['COD_CURSO','MATRICULA']].groupby('COD_CURSO')

	for cod, curso in cursos:	# Itera o agrupamento passando por cada curso.
		listaAlunos = curso.MATRICULA	# Guarda a lista de aluno referente ao curso.

		# Cria o objeto curso com o codigo do curso e a lista de alunos do curso.
		objetoCurso = Curso(cod, listaAlunos)	

		# Add o objetoCurso na lista de cursos.
		listaCursos.append(objetoCurso)	

	return listaCursos	# Retorna a lista de objetos curso.

def CalculoCR(listaAluno):
	listaCR = []
	listaMatricula = []
	print('------- O CR dos alunos é: -------')
	for aluno in listaAluno:
		# Executa o método .calculoCR no objeto aluno que retorna o CR de cada aluno.
		Cr = aluno.calculoCR()

		# Método Get que retorna o codigo da matrícula.
		matricula = aluno.getMatricula()

		# Add do cr e codigo da matrícula em listas.
		listaCR.append(Cr)	
		listaMatricula.append(matricula)

		print(f'{matricula}  -  {Cr}')
	print('----------------------------------')
	return listaMatricula, listaCR # Retorna as listas de CR e Matrícula.

def mediaCRCurso(listaCurso, listaMatriculas, listaCR):
	listaCrCurso = []
	listaCodCurso = []
	print('----- Média de CR dos cursos ------')
	# Itera entre os objetos curso.
	for curso in listaCurso:
		somaCR = 0
		somaAluno = 0
		for aluno in curso.getListaAlunos(): # Itera entre a lista de alunos de cada curso.
			# Carrega o index do aluno com base na lista de matriculas.
			indexMatricula = listaMatriculas.index(aluno)	

			# É utilizado o CR da listaCR com o index da lista de matrículas visto que são equivalentes.
			somaCR = somaCR + listaCR[indexMatricula]
			somaAluno += 1
		
		crCurso = round(somaCR/somaAluno) # Calcula e arredonda o CR médio do curso.

		# Add do CR médio e do codigo do curso em listas.
		listaCrCurso.append(crCurso) 				
		listaCodCurso.append(curso.getCodCurso())	
		print(f'{curso.getCodCurso()} - {crCurso}')
	print('----------------------------------')
	return listaCodCurso, listaCrCurso	# Retorna as listas de CR médio e código de curso.


