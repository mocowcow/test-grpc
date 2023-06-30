import os
import grpc

import file_transport_pb2_grpc
import file_transport_pb2

FILE_PATH = "./download"


channel = grpc.insecure_channel('localhost:19810')
stub = file_transport_pb2_grpc.FileServiceStub(channel)

request = file_transport_pb2.DownloadRequest()
request.filename = "ffff.txt"
response = stub.Download(request)

path = os.path.join(FILE_PATH, request.filename)
with open(path, "wb") as bin_file:
    bin_file.write(response.body)

print(response.result)
