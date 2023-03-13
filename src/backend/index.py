from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares

def main(event, context):
    for key in allMiddlewares:
        if not allMiddlewares[key]['isTriggered']:
            continue
        return allMiddlewares[key]['getResponse'](event, allDialogs)

    for key in allDialogs:
        if not allDialogs[key]['isTriggered']:
            continue
        return allDialogs[key]['getResponse'](event, context)


app = Flask(__name__)

@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    print(data)
    reqzap = main(data, None)
    return reqzap


if __name__ == '__main__':
    print('Server starting...')
    app.run(port=2083, host='0.0.0.0', debug=True)
    print('Server started successfully!')
