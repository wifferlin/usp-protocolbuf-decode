#!/bin/bash

Dest_folder="build"
Src_folder="def"

for FILE in "$Src_folder/*"
do
	echo $FILE
	protoc --proto_path=$Src_folder --python_out=$Dest_folder $FILE
done

#protoc --proto_path=src --python_out=build/ src/usp-msg.proto src/usp-record.proto
