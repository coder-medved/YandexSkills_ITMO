from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    print(data)
    return 'Данные успешно получены'


if __name__ == '__main__':
    app.run()