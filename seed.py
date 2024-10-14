from app import app, db
from models import Hero, Power

with app.app_context():
    hero1 = Hero(name='Kelvin', super_name='Kamau')
    hero2 = Hero(name='Joyce', super_name='Njeri')
    power1 = Power(name='super strength', description='gives the wielder super-human strengths')
    power2 = Power(name='flight', description='gives the wielder the ability to fly through the skies at supersonic speed')
    
    db.session.add_all([hero1, hero2, power1, power2])
    db.session.commit()
