# Flask / flask_login / flask_sqlalchemy
[Tutorial login/flask](https://www.youtube.com/watch?v=vRgay-IXeek)
[Tutorial jwt/flask](https://www.youtube.com/watch?v=z92CWqvefr0)

Dicas rápidas:
- Rotas são criadas com `@app.route('/', methods=['GET', 'POST' ... ])`
- Sistema de login utilizando `flask_login` e `flask_sqlalchemy`
- Sistema de authenticação utilizando `flask_marshmallow` para serialização do `model.User`

Configurações \
✅ Servidor configurado para servir SPA na pasta `public` | [doc](https://flask.palletsprojects.com/en/2.0.x/patterns/singlepageapplications/)
✅ Rotas configuráveis com guard pelo decotador `@jwt_required` acima da configuração da rota;
✅ login por json e por form
✅ registro por json e por form