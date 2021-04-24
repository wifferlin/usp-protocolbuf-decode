# usp-protocolbuf-decode
A tool that can decode USP Record and USP Message 

2021/04/22 Wiffer Lin
This tool can decode the usp data that use protocol buffer to encode.
Include USP Record and USP Message.

1. Put the protocol buffer define into def/ folder. (usp-record.proto, usp-msg.proto)

2. Please use shell script to generate the python code in the first time. (If change define need re-generate.)
        * Need to install compiler first.
                * sudo apt-get install protobuf-compiler
        * ./gen_py_code.sh
   This Script will create python use code in build/ folder.

3. Put the encode data into "encode_src" file (Can Get from wireshark.)

4. Use decode.py to decode protocol buffer value and get the json result on "decode_result" file.
        * python3 decode.py
