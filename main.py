from flask import render_template, request, redirect, url_for, jsonify, Response
from flask_login import login_user, logout_user, current_user
from app import app, db
from app.models import User, user_share_schema, users_share_schema
from app.security import jwt_required
import jwt
import datetime

###########################################################################
#                                                                         #
# Sistema de login                                                        #
#                                                                         #

@app.route('/form/register', methods=['GET', 'POST'])
def formRegister():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        pwd = request.json['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()

    result = user_share_schema(
        User.query.filter_by(email=email).first()
    )

    return jsonify(result)

# JSON:
# {
#     "email": "xxx@x.com",
#     "password": "1234"
# }
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.json['email']
        pwd = request.json['password']

        user = User.query.filter_by(email=email).first_or_404()

        if not user or not user.verify_password(pwd):
            return jsonify({ "error" : "Suas credenciais estão erradas"}), 403
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }

        token = jwt.encode(payload, app.config['SECRET_KEY'])

        return jsonify({"access_token": token})

    return render_template('login.html')

@app.route('/form/login', methods=['GET', 'POST'])
def formLogin():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

#                                                                         #
#                                                                         #
#                                                                         #
###########################################################################



###########################################################################
#                                                                         #
#   Rotas da API                                                          #
#                                                                         #

@app.route('/hellojson')
@jwt_required
def hello_json(current_user):
    if current_user.is_authenticated:
        # code loged go here;
        return jsonify({"msg":"hello json!"})
    else:
        return Response("Não logado", 401)

@app.post('/get_json')
@jwt_required
def get_json():
    if current_user.is_authenticated:
        content = request.json
        print(content)
        return content
    else:
        return Response("Não logado", 401)

#                                                                         #
#                                                                         #
#                                                                         #
###########################################################################



###########################################################################
#                                                                         #
# Sistema SPA                                                             #
#                                                                         #

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

with app.app_context():
    db.create_all()

#                                                                         #
#                                                                         #
#                                                                         #
###########################################################################

app.run(debug=True)