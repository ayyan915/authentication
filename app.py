from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth import auth


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "AYYAN2009"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_CSRF_PROTECT"] = False
jwt = JWTManager(app)

app.register_blueprint(auth)
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)