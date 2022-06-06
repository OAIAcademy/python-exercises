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


@app.get('/es1')
def es_1():
    return "test"


@app.get('/es2')
def es_2():
    # lettura parametri, il metodo get del dizionario permette di inpostare un valore di default se la chiave è
    # assente (utile ad evitare eccezioni)
    x = request.args.get("x", 0)
    y = request.args.get("y", 0)
    return str(x + y)


@app.post('/es3')
def es_3():
    d = request.get_json()
    par = request.args.get("filter", '')
    # ciclo su chivi del dizionario
    for k in d.keys():
        # controlla cob in se la strigha par è una sottostringa di k
        if par in k:
            d[k] = 0
    return d


if __name__ == '__main__':
    app.run(port=3333)
