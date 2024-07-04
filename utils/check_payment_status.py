import json
import uuid
from flask import jsonify
import requests
import hmac
import hashlib


def check_payment_status():
    # Create response body
    # response_body = {
    #     "partnerCode": partnerCode,
    #     "requestId": requestId,
    #     "orderId": orderId,
    #     "resultCode": resultCode,
    #     "message": message,
    #     "responseTime": responseTime,
    #     "extraData": extraData,
    #     "signature": signature
    # }
    response_body = {
        "resultCode": 0,
    }
    print("chay do dc inp")

    response = jsonify(response_body)
    response.status_code = 204
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response
