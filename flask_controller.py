from flask import Flask, request

app = Flask(__name__)


@app.get('/hello')
def hello():
    return 'Hello, World!'


@app.post('/')
def test():
    print(request.get_json())
    print(request.headers)
    print(request.args)
    return request.get_json()


if __name__ == '__main__':
    app.run(port=3333)
