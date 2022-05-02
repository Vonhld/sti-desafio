# Ferramenta Flask foi utilizada e um template com bootstrap foi criado.
from flask import Flask, render_template
from base import GUIAlunos, GUIACursos

app = Flask(__name__) 

@app.route('/') 
def main():
  return render_template('template.html', alunos = GUIAlunos, cursos = GUIACursos)

if __name__ == '__main__':
  app.run(debug=True) 