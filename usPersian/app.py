import datetime
import json
#import requests
#import boto3
import uuid
#from send_email import send_email
#from botocore.exceptions import ClientError


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    print(event)
    print('******************************')
    print('******************************')
    if event['httpMethod'] == 'GET':
        return get_ip(event, context)
    elif event['httpMethod'] == 'POST':
        temp = sign_in(event, context)
        print(temp)
        print('1234 test')
        data = {
            'status': 200,
            "body": json.dumps(temp)
        }
        return data


def get_ip(event, context):

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        }),
    }


def sign_in(event, context):
    ip = requests.get("http://checkip.amazonaws.com/")
    id = uuid.uuid1()
    params = event.get('queryStringParameters')
    print('params------')
    print(params)
    print('prams======')
    item = {
        'body': event['body'],
        'itemId': id.urn[9:],
        'userName': 'musavi1',
        'creatDate': datetime.datetime.now()

    }

    dynamodb = boto3.client('dynamodb')
    current_time = datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S)")
    dynamodb.put_item(TableName='usPersianLogin',
                      Item={'userName':
                                {'S': 'musavi1'},
                            'createdDate':
                                {'S': current_time},
                            'body':
                                {'S': item['body']},
                            'itemId':
                                {'S': item['itemId']}
                            })
    send_email(params)
    data = {
        "statusCode": 200,
        "body": {
            "message": "Email sent successfully",
            "location": ip.text.replace("\n", "")
        },
    }
    return data
