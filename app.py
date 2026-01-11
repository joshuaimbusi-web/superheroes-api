from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from config import Config, db, migrate
from models import Hero, Power, HeroPower

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

mail = Mail(app)


@app.get("/heroes")
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([h.to_dict(only=("id", "name", "super_name")) for h in heroes]), 200


@app.get("/heroes/<int:id>")
def get_hero_by_id(id):
    hero = Hero.query.get(id)
    if not hero:
        return {"error": "Hero not found"}, 404
    return jsonify(hero.to_dict()), 200


@app.get("/powers")
def get_powers():
    powers = Power.query.all()
    return jsonify([p.to_dict() for p in powers]), 200


@app.get("/powers/<int:id>")
def get_power_by_id(id):
    power = Power.query.get(id)
    if not power:
        return {"error": "Power not found"}, 404
    return jsonify(power.to_dict()), 200


@app.patch("/powers/<int:id>")
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return {"error": "Power not found"}, 404

    try:
        data = request.get_json()
        power.description = data.get("description")
        db.session.commit()
        return jsonify(power.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 422


@app.post("/hero_powers")
def create_hero_power():
    try:
        data = request.get_json()
        hero_power = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(hero_power)
        db.session.commit()

        return jsonify(hero_power.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return {"errors": [str(e)]}, 422
    

@app.get("/test-email")
def test_email():
    msg = Message(
        subject="Flask-Mail Test",
        recipients=["recipient@example.com"],
        body="Flask-Mail is configured and working."
    )
    mail.send(msg)
    return {"message": "Email sent successfully"}, 200



if __name__ == "__main__":
    app.run(port=5555, debug=True)
