import json
import uuid
import requests
import hmac
import hashlib


def query_payment(orderId,):
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/query"
    accessKey = "F8BBA842ECF85"
    secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
    orderInfo = "pay with MoMo"
    partnerCode = "MOMO"
    redirectUrl = "tshop://"
    ipnUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
    requestId = orderId
    extraData = ""  # pass empty value or Encode base64 JsonString
    requestType = "captureWallet"
    lang = "vi"
    
    rawSignature = f"accessKey={accessKey}&orderId={orderId}" \
                   f"&partnerCode={partnerCode}" \
                   f"&requestId={requestId}"
    print(rawSignature)

    # signature
    h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()

    data = {
        "partnerCode": partnerCode,
        "requestId": requestId,
        "orderId": orderId,
        "signature": signature,
        "lang": lang
    }
    
    response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})
    
    return response.json()
    
    
