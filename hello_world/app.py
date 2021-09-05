import json
import base64
import cv2
import numpy as np

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

    # return {
    #     "statusCode": 200,
    #     "body": json.dumps(
    #         {
    #             "message": "hello world",
    #         }
    #     ),
    # }
    src_bytes = base64.b64decode(event["body"])
    src = cv2.imdecode(np.frombuffer(src_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, gray_bytes = cv2.imencode(".jpg", gray)

    return {
        "statusCode": 200,
        "body": json.dumps(base64.b64encode(gray_bytes).decode("UTF-8")),
    }
