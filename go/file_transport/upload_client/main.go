package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"time"

	pb "file_transport/proto"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

var (
	addr = flag.String("addr", "localhost:19810", "the address to connect to")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewFileServiceClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	request := pb.UploadRequest{}
	request.Filename = "1111.txt"
	var body []byte = []byte{}
	request.Body = body
	fmt.Println(&request)

	response, err := c.Upload(ctx, &request)
	if err != nil {
		fmt.Println("upload failed")
	} else {
		fmt.Println(response)
	}

}
