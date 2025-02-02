import json
from config.sqs_client import SQSClient
from services.message_service import process_message

def receive_messages():
    sqs_client = SQSClient()
    
    while True:
        messages = sqs_client.receiveMessages()
        print('Received messages:', messages)
        for message in messages:
            message_body = json.loads(message["Body"])
            receipt_handle = message["ReceiptHandle"]
            message_content = message_body["message"]
            print('Message body', message_body)
            
            response = process_message(message_content)
            
            if response:
                sqs_client.sendMessage(json.dumps(response))
                
            sqs_client.deleteMessage(receipt_handle)