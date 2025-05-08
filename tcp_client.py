# src/client/client.py
import socket
import sys

class TupleSpaceClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        """连接服务器"""
        pass

    def send_request(self, request):
        """发送请求到服务器"""
        pass

    def process_file(self, file_path):
        """处理请求文件"""
        pass
