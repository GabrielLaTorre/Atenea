import boto3
import os
from dotenv import load_dotenv

load_dotenv()

class SQSClient:
    def __init__(self):
        self.sqs = boto3.client(
            'sqs',
             region_name=os.getenv('AWS_REGION'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

    def receiveMessages(self):
        response = self.sqs.receive_message(
            QueueUrl=os.getenv('INCOMING_MESSAGE_QUEUE_URL'),
            AttributeNames=['All'],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10
        )
        return response.get('Messages', [])

    def deleteMessage(self, receipt_handle):
        self.sqs.delete_message(
            QueueUrl=os.getenv('INCOMING_MESSAGE_QUEUE_URL'),
            ReceiptHandle=receipt_handle
        )

    def sendMessage(self, respuesta):
        response = self.sqs.send_message(
            QueueUrl=os.getenv('OUTGOING_MESSAGE_QUEUE_URL'),
            MessageBody=respuesta
        )
        return response['MessageId']
