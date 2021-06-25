from google.protobuf import text_format
from google.protobuf.message import DecodeError
from build import usp_record_pb2 as Record
from build import usp_msg_pb2 as Msg

DEBUG_FLAG = 0

def decode_usp_record (encode_hex):
	bytes_record = bytes.fromhex(encode_hex)
	my_record = Record.Record()
	my_record.ParseFromString(bytes_record)
	
	record_type = my_record.WhichOneof('record_type')
	if DEBUG_FLAG > 0:
		print("\nSession_context Payload:")
		print(my_record.session_context.payload)
		print("\nNo_Session_context Payload:")
		print(my_record.no_session_context.payload)

	if record_type == "session_context" :
		record_payload = my_record.session_context.payload[0]
	if record_type == "no_session_context" :
		record_payload = my_record.no_session_context.payload
	
	if DEBUG_FLAG > 0:
		print("\nRecord Hex:\n" + encode_hex)
		print("\nRecord Bytes String:")
		print(bytes_record)
	print("\nRecord Json:")
	print(my_record)
	return record_payload

def decode_usp_msg (record_payload):
	my_msg = Msg.Msg()
	my_msg.ParseFromString(record_payload)

	if DEBUG_FLAG > 0:
		print("Msg Bytes String:")
		print(record_payload)
	print("\nMsg Json:")
	print(my_msg)

if __name__ == '__main__':
	# Read encode hex string
	f = open('encode_src','r')
	contents = f.readline()
	if DEBUG_FLAG > 1:
		print("Contents:")
		print(contents)
	f.close()

	# Decode Record 
	record_payload = decode_usp_record(contents)
	
	# Decode Msg
	decode_usp_msg(record_payload)
