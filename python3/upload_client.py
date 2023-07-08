import grpc

import file_transport_pb2_grpc
import file_transport_pb2


channel = grpc.insecure_channel('localhost:19810')
stub = file_transport_pb2_grpc.FileServiceStub(channel)

request = file_transport_pb2.UploadRequest()
request.filename = "grpc_test.txt"
request.body = b"hello python"

response = stub.Upload(request)
print(response)
