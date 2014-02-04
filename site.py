from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


@app.route("/")
def get_my_ip():
    if not request.headers.getlist("X-Forwarded-For"):
        return request.remote_addr
    else:
        return request.headers.getlist("X-Forwarded-For")[-1]


@app.route("/useragent")
def useragent():
    return request.headers.get("User-Agent")


@app.route("/headers")
def headers():
    return jsonify(request.headers), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
