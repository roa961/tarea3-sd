from flask import Flask, request, render_template, app

import proto_web_pb2 as pb2
import proto_web_pb2_grpc as pb2_grpc
import grpc
import time

app = Flask(__name__)


class Cliente(object):
    def __init__(self):
        self.host = "servidor"
        self.port = "50051"
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.port))
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_palabra(self, message):
        message = pb2.Message(message=message)
        print(f'{message}')
        stub = self.stub.GetServerResponse(message)
        return stub


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def busqueda():
    cliente = Cliente()
    search = request.args['search']
    web = cliente.get_palabra(message=search)
    return render_template('index.html', datos=web, )


if __name__ == "__main__":
    time.sleep(20)
