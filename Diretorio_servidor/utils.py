import os
import json

def extract_route(req):
    print(req.split())
    return req.split()[1][1:]


def read_file(path):
    nome1,nome2 = os.path.splitext(path)

    lista_arq = [".txt", ".html", ".css",".js"]

    if nome2 in lista_arq:
        f = open(path, "rt")
        return f.read()
    else:
        f = open(path,"rb")
        return f.read()

def load_data(path):
    with open("data/" + path) as arq_json:
        return json.load(arq_json) 

def load_template(path):
    path = "templates/" + path
    return read_file(path)

def build_response(body='', code=200, reason='OK', headers=''):
    response = 'HTTP/1.1 ' + (' '.join([str(code), reason]))
    
    if headers == '':
        response += '\n\n' + body
    else:
        response += '\n' + headers + '\n\n' + body

    print('Response: ' + response)
    
    return response.encode()