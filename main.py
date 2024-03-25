from flask import render_template, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

# @app.route('/')
# def home():
#     return render_template('home.html')

###########################################################################
#                                                                         #
# Sistema de login                                                        #
#                                                                         #

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['password']

        user = User(name, email, pwd)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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
def hello_json():
    return jsonify({"msg":"hello json!"})

@app.post('/get_json')
def get_json():
    content = request.json
    print(content)
    return content
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