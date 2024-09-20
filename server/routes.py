from flask import jsonify
from server.app import app, db
from server.models import Animal, Zookeeper, Enclosure

@app.route('/animal/<int:id>', methods=['GET'])
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    return jsonify({
        'id': animal.id,
        'name': animal.name,
        'species': animal.species,
        'zookeeper': animal.zookeeper.name,
        'enclosure': animal.enclosure.environment
    })

@app.route('/zookeeper/<int:id>', methods=['GET'])
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    return jsonify({
        'id': zookeeper.id,
        'name': zookeeper.name,
        'birthday': zookeeper.birthday,
        'animals': [animal.name for animal in zookeeper.animals]
    })

@app.route('/enclosure/<int:id>', methods=['GET'])
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    return jsonify({
        'id': enclosure.id,
        'environment': enclosure.environment,
        'open_to_visitors': enclosure.open_to_visitors,
        'animals': [animal.name for animal in enclosure.animals]
    })
