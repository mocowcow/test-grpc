set go="./go"

python -m grpc_tools.protoc --python_out=go --pyi_out=go --grpc_python_out=go  -I . *.proto