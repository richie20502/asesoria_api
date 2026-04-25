from flask import Blueprint, request, jsonify, current_app
from models.user import User


user_bp = Blueprint('user', __name__, url_prefix='/users')


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']  # luego encriptamos
    )
    db = current_app.extensions['sqlalchemy']

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuario creado"}), 201