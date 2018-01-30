# pip install Flask

# jsonfy é um helper que transforma em JSON
# request é um objeto que possui os dados da requisição
from flask import Flask, jsonify, request
from person import Person

app = Flask(__name__)

# API Index
@app.route('/')
def index():
    return jsonify({ 'status': 404, 'mensagem': 'Este é o meu web API de Pessoas.' })

# GET /persons/
@app.route('/persons')
def persons():
    return jsonify([person.to_dictionary() for person in Person.select()])

# GET /persons/1
@app.route('/persons/<int:id>')
def person(id):
    try:
        person = Person.get(id = id)
        return jsonify(person.to_dictionary())

    except Person.DoesNotExist:
        return jsonify({ 'status': 404, 'mensagem': 'Pessoa não encontrada.' })

# POST /persons/
@app.route('/persons', methods = ['POST'])
def new_person():
    try:
        person = Person(name = request.json['name'], age = request.json['age'])
        person.save()
        return jsonify({ 'status': 200, 'mensagem': 'Pessoa salva com sucesso.' })
    except Exception as e:
        return jsonify({ 'status': 404, mensagem: 'Ocorreu algum erro inesperado'})

# PUT/PATCH /persons/1
@app.route('/persons/<int:id>', methods = ['PUT', 'PATCH'])
def editar_postagem(id):
    try:
        person = Person.get(id = id)

    except Person.DoesNotExist as e:
        return jsonify({'status': 404, 'mensagem': 'Pessoa não encontrada.'})

    person.name = request.json['name']
    person.age = request.json['age']
    person.save()
    return jsonify({'status': 200, 'mensagem': 'Pessoa salva com sucesso.'})

# DELETE /persons/1
@app.route('/persons/<int:id>', methods = ['DELETE'])
def apagar_postagem(id):
    try:
        person = Person.get(id = id)
        person.delete_instance()
        return jsonify({'status': 200, 'mensagem': 'Pessoa excluída com sucesso'})

    except Person.DoesNotExist:
        return jsonify({'status': 404, 'mensagem': 'Pessoa não encontrada'})

if __name__ == '__main__':
    app.run(debug = True)