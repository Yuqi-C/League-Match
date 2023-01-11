#server.py

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
import json
import os

err = 0
req = 0

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def anagrams(input):
    length = len(input)
    freq = [0] * 26
    for i in range(0, length):
        if(input[i] >= 'a' and input[i] <= 'z'):
            freq[ord(input[i])-97] += 1
        elif(input[i] >= 'A' and input[i] <= 'Z'):
            freq[ord(input[i])-65] += 1
        else:
            return 0
    res = 1
    for element in freq:
        res *= factorial(element)
    return factorial(length) // res                           


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global req
        global err
        req += 1
        path, _, query_string = self.path.partition("?")

        if path == '/ping':
            self.send_response(204)
            self.end_headers()
            self.wfile.write(b'')
        elif path == '/anagram':
            query = parse_qs(query_string) 
            if(len(query) == 0):
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'')
            else:
                num = anagrams(query['p'])
                query['total'] = num
                jsonStr = json.dumps(query)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(jsonStr.encode()) 
        elif path == '/secret':
            try:
                body = open('/tmp/secret.key','r').read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(body.encode())
            except:
                err += 1
                self.send_response(404)
                self.end_headers()
        elif path == '/status':
            today = datetime.now()
            iso_date = today.isoformat()
            dict = {'time' : iso_date, 'req' : str(req), 'err' : str(err)}
            jsonStr = json.dumps(dict)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(jsonStr.encode())
        else:
            err += 1
            self.send_response(404)
            self.end_headers()

httpd = HTTPServer(('localhost', 8088), MyHTTPRequestHandler) 
httpd.serve_forever()
