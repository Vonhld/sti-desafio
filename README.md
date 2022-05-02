## Sobre
Projeto referente a resolução do desafio proposto pela Superintendência de Tecnologia da Informação, STI, da Universidade Federal Fluminense.

O desafio 3 foi escolhido dentre as possibilidades em
* https://github.com/sti-uff/trabalhe-conosco/blob/master/Desafios.md

## Desafio 3

Você precisa calcular o CR de alunos de uma universidade. Para isto será preciso ler de um [arquivo csv](dataset/notas.csv) a lista de notas dos alunos e, de acordo com as notas e os critérios da universidade, calcular o CR de todos os alunos. Ao final do processo, será preciso mostrar na tela o CR de todos os alunos e qual a média de CR dos cursos.

### Regras
* A nota do aluno vai de zero até 100;
* Uma nota é associada a uma disciplina e a um código de curso;
* O CR é a média ponderada da nota do aluno naquela turma com a carga horária daquela turma. O cálculo é:
  * > CR = Nota(i)*CargaHoraria(i)/TotalCargaHoraria 
  * i é a i-ésima turma de um aluno
* Utilizar Orientação a Objetos para resolver o problema
* Escolha a linguagem que achar adequada

### Exemplo
Após executar a sua aplicação, o sistema deve exibir uma saída similar a:

```bash
------- O CR dos alunos é: --------
100  -  10 
101  -  11
...
116  -  26
-----------------------------------
----- Média de CR dos cursos ------
10   -  12
11   -  45
..
100  -  13
-----------------------------------
```

## Resolução
Para a resolução, a linguagem Python (3.9.7) foi utilizada, assim como as bibliotecas a seguir.

* **Pandas**, para analisar e manipular o dataset dado.
```bash 
  pip install pandas
```
* **Flask**, para criação de um GUI utilizando o framework de Bootstrap.
```bash 
  pip install pandas
```

#### Sobre os arquivos

* **[aluno.py](classes/aluno.py)**, **[curso.py](classes/curso.py)** e **[nota.py](classes/nota.py)** referentes as classes utilizadas.

* **[manipulaDados.py](manipulaDados.py)** referente ao carregamento e manipulação dos dados.

* **[base.py](base.py)** referente ao controlador que chama os métodos.

* **[GUI.py](GUI.py)** referente a GUI

* **[template.html](templates/template.html)** referente ao framework web utilizando Bootstrap.

* **aluno.py**, **curso.py** e **nota.py** referentes as classes utilizadas.

* **trabalhaDados.py** referente ao carregamento e manipulação dos dados.

* **base.py** referente ao controlador que chama os métodos.

* **GUI.py** referente a GUI

* **template.html** referente ao framework web utilizando Bootstrap.