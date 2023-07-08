package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"os"
	"path"
	"time"

	pb "file_transport/proto"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const folderPath = "./download"

var (
	addr = flag.String("addr", "localhost:19810", "the address to connect to")
)

func main() {
	_ = os.MkdirAll(folderPath, os.ModePerm)

	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewFileServiceClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*2)
	defer cancel()
	request := pb.DownloadRequest{}
	request.Filename = "grpc_test.txt"
	fmt.Println(&request)

	response, err := c.Download(ctx, &request)
	if err != nil {
		fmt.Println("download failed")
		fmt.Println(err)
	} else {
		filepath := path.Join(folderPath, request.Filename)
		_ = os.WriteFile(filepath, response.Body, os.ModePerm)
	}

}
