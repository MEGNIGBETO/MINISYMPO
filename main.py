from app import app
from auth import auth

app.register_blueprint(auth, url_prefix='/')

if __name__ == '__main__':
    app.run(port=3000)
