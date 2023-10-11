from flask import Flask

from views.routesTech import tech

app = Flask(__name__)
app.register_blueprint(tech, url_prefix="/tech")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)