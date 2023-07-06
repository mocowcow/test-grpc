package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"
	"os"
	"path"

	pb "file_transport/proto"

	"google.golang.org/grpc"
)

const filepath = "./upload"

var (
	port = flag.Int("port", 19810, "The server port")
)

type server struct {
	pb.UnimplementedFileServiceServer
}

func (s *server) Upload(ctx context.Context, in *pb.UploadRequest) (*pb.UploadResponse, error) {
	err := os.WriteFile(path.Join(filepath, in.Filename), in.Body, 0644)

	if err != nil {
		return nil, err
	}

	res := pb.UploadResponse{Result: "ok"}

	return &res, nil
}

func (s *server) Download(ctx context.Context, in *pb.DownloadRequest) (*pb.DownloadResponse, error) {
	body, err := os.ReadFile(path.Join(filepath, in.Filename))

	if err != nil {
		return nil, err
	}

	res := pb.DownloadResponse{Result: "ok", Body: body}

	return &res, nil

}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterFileServiceServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
