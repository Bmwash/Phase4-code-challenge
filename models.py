from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    hero_powers = relationship('HeroPower', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }

class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    hero_powers = relationship('HeroPower', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    
    hero = relationship('Hero', back_populates='hero_powers')
    power = relationship('Power', back_populates='hero_powers')

    def to_dict(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
            'hero': self.hero.to_dict(),
            'power': self.power.to_dict()
        }

    @db.validates('strength')
    def validate_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        return strength

    @db.validates('power_id')
    def validate_power(self, key, power_id):
        power = Power.query.get(power_id)
        if not power:
            raise ValueError("Power does not exist")
        return power_id
