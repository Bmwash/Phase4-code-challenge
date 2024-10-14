from flask import Blueprint, jsonify, request
from models import Hero, Power, HeroPower, db

api = Blueprint('api', __name__)

@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict())

@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@api.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict())

@api.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power not found"}), 404

    data = request.json
    try:
        power.description = data.get('description', power.description)
        db.session.commit()
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

    return jsonify(power.to_dict())

@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hero_power)
        db.session.commit()
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

    return jsonify(hero_power.to_dict()), 201
