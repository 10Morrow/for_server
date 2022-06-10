# -*- coding: utf-8 -*-
import chardet
import socket
import json
import ssl
import urllib3
from io import BytesIO
from http.client import HTTPResponse
CRLF = '\r\n'
SP = ' '
CR = '\r'

class BytesIOSocket:
    def __init__(self, content):
        self.handle = BytesIO(content)

    def makefile(self, mode):
        return self.handle

def response_from_bytes(data):
    sock = BytesIOSocket(data)

    response = HTTPResponse(sock)
    try:
   	 response.begin()
    except:
        print("pass")
    return urllib3.HTTPResponse.from_httplib(response)

def start_my_server():
	print("server start")
	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind(('',  8443))
		server.listen(1)
		while True:
			client_socket, address = server.accept()
			print('Connected with ', address)
			try:
				data = client_socket.recv(4096)
			except:
				print("encode error")
			return_client_data(data)
			client_socket.shutdown(socket.SHUT_WR)
			client_socket.close()
	except KeyboardInterrupt:
		server.close()
		print("Сервер был выключен...")


def return_client_data(request):
	try:
		request = json.loads(request)
		print(request)
	except:
		print(type(request))
		data_ = response_from_bytes(request)
		print(data_.headers)
		print(data_.data)
if __name__ == '__main__':
	start_my_server()
