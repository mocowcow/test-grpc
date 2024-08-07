import os
import grpc
from concurrent import futures

import file_transport_pb2_grpc
import file_transport_pb2

FILE_PATH = "./upload"

if not os.path.isdir(FILE_PATH):
    os.mkdir(FILE_PATH)


class FileTransportServicer(file_transport_pb2_grpc.FileServiceServicer):
    def Upload(self, request, context):
        path = os.path.join(FILE_PATH, request.filename)
        with open(path, "wb") as bin_file:
            bin_file.write(request.body)
        response = file_transport_pb2.UploadResponse()  # pylint: disable=no-member
        response.result = "ok"
        print("got a file", request.filename)
        return response

    def Download(self, request, context):
        path = os.path.join(FILE_PATH, request.filename)
        response = file_transport_pb2.DownloadResponse()  # pylint: disable=no-member
        with open(path, "rb") as bin_file:
            body = bin_file.read()
            response.body = body
        response.result = "ok"
        print("send a file", request.filename)
        print(path, response.body)
        return response


def serve():
    port = "19810"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_transport_pb2_grpc.add_FileServiceServicer_to_server(
        FileTransportServicer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
