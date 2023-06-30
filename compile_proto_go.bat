set go="./go"

protoc -I="." "*.proto" ^
--go_out=%go% ^
--go-grpc_out=%go%

