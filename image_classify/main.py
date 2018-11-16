from google.cloud import storage
from google.cloud import vision
import json


def handle_event(event, context):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(event['bucket'])
    blob = bucket.blob(event['name'])
    print('checking blob {} in bucket {}'.format(event['name'], event['bucket']))
    print('public url is {}'.format(blob.public_url))

    vision_client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = blob.public_url

    response = vision_client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    print('Labels:{}'.format(','.join(labels)))

    blob.metadata = {'labels': ','.join(labels)}
    blob.patch()
