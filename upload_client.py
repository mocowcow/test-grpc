import os
import grpc
from concurrent import futures

import file_transport_pb2_grpc
import file_transport_pb2


channel = grpc.insecure_channel('localhost:19810')
stub = file_transport_pb2_grpc.FileServiceStub(channel)

request = file_transport_pb2.UploadRequest()
request.filename = "ffff.txt"
request.body = b'\x21\x21\x21\x21'


response = stub.Upload(request)
print(response)
