import os
import grpc
from concurrent import futures

import file_transport_pb2_grpc
import file_transport_pb2

FILE_PATH = "./files"


class FileTransportServicer(file_transport_pb2_grpc.FileServiceServicer):
    def Upload(self, request, context):
        path = os.path.join(FILE_PATH, request.filename)
        with open(path, "wb") as bin_file:
            bin_file.write(request.body)
        response = file_transport_pb2.UploadResponse()
        response.result = "ok"
        print("got a file",request.filename)
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
