from functools import wraps
from flask import request, jsonify, current_app
from app.models import User
import jwt
# import traceback

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'authorization' in request.headers:
            token = request.headers['authorization']
        
        if not token:
            return jsonify({ "error": "Você não está autorizado!"}), 403
        
        if not "Bearer" in token:
            return jsonify({ "error": "Token inválido!"}), 401
        
        try:
            token_pure = token.replace("Bearer ","")
            decoded = jwt.decode(token_pure, current_app.config['SECRET_KEY'], algorithms='HS256')
            current_user = User.query.get(decoded['id'])
        except:
            # traceback.print_exc()
            return jsonify({"error": "O token é inválido"}), 401

        return f(current_user=current_user, *args, **kwargs)
    
    return wrapper