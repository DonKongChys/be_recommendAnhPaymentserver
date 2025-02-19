import json
import uuid
import requests
import hmac
import hashlib

def create_payment_request(order_id, amount):
    # parameters send to MoMo get payUrl
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
    accessKey = "F8BBA842ECF85"
    secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
    orderInfo = "pay with MoMo"
    partnerCode = "MOMO"
    redirectUrl = "tshop://"
    ipnUrl = "https://be-recommendanhpaymentserver.onrender.com/tshop/momo_ipn"
    requestId = order_id
    extraData = ""  # pass empty value or Encode base64 JsonString
    partnerName = "MoMo Payment"
    requestType = "captureWallet"
    storeId = "tshop"
    orderGroupId = ""
    autoCapture = True
    lang = "vi"
    orderGroupId = ""
    orderExpireTime = 1

    # before sign HMAC SHA256 with format: accessKey=$accessKey&amount=$amount&extraData=$extraData&ipnUrl=$ipnUrl
    # &orderId=$orderId&orderInfo=$orderInfo&partnerCode=$partnerCode&redirectUrl=$redirectUrl&requestId=$requestId
    # &requestType=$requestType
    rawSignature = f"accessKey={accessKey}&amount={amount}&extraData={extraData}&ipnUrl={ipnUrl}&orderId={order_id}" \
                   f"&orderInfo={orderInfo}&partnerCode={partnerCode}&redirectUrl={redirectUrl}" \
                   f"&requestId={requestId}&requestType={requestType}"
    # print(rawSignature)
    

    # signature
    h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()

    # json object send to MoMo endpoint
    data = {
        'partnerCode': partnerCode,
        'orderId': order_id,
        'partnerName': partnerName,
        'storeId': storeId,
        'ipnUrl': ipnUrl,
        'amount': amount,
        'lang': lang,
        'requestType': requestType,
        'redirectUrl': redirectUrl,
        'autoCapture': autoCapture,
        'orderInfo': orderInfo,
        'requestId': requestId,
        'extraData': extraData,
        'signature': signature,
        'orderGroupId': orderGroupId,
        'orderExpireTime': orderExpireTime
    }

    response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})

    return response.json()

def create_payment_cc_request(order_id, amount):
    # parameters send to MoMo get payUrl
    endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
    accessKey = "F8BBA842ECF85"
    secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
    orderInfo = "pay with MoMo"
    partnerCode = "MOMO"
    redirectUrl = "tshop://"
    ipnUrl = "https://be-recommendanhpaymentserver.onrender.com/tshop/momo_ipn"
    requestId = order_id
    extraData = ""  # pass empty value or Encode base64 JsonString
    partnerName = "MoMo Payment"
    requestType = "payWithCC"
    storeId = "tshop"
    orderGroupId = ""
    autoCapture = True
    lang = "vi"
    orderGroupId = ""
    # orderExpireTime = 60
    

    # before sign HMAC SHA256 with format: accessKey=$accessKey&amount=$amount&extraData=$extraData&ipnUrl=$ipnUrl
    # &orderId=$orderId&orderInfo=$orderInfo&partnerCode=$partnerCode&redirectUrl=$redirectUrl&requestId=$requestId
    # &requestType=$requestType
    rawSignature = f"accessKey={accessKey}&amount={amount}&extraData={extraData}&ipnUrl={ipnUrl}&orderId={order_id}" \
                   f"&orderInfo={orderInfo}&partnerCode={partnerCode}&redirectUrl={redirectUrl}" \
                   f"&requestId={requestId}&requestType={requestType}"
    # print(rawSignature)
    

    # signature
    h = hmac.new(bytes(secretKey, 'ascii'), bytes(rawSignature, 'ascii'), hashlib.sha256)
    signature = h.hexdigest()

    # json object send to MoMo endpoint
    data = {
        'partnerCode': partnerCode,
        'orderId': order_id,
        'partnerName': partnerName,
        'storeId': storeId,
        'ipnUrl': ipnUrl,
        'amount': amount,
        'lang': lang,
        'requestType': requestType,
        'redirectUrl': redirectUrl,
        'autoCapture': autoCapture,
        'orderInfo': orderInfo,
        'requestId': requestId,
        'extraData': extraData,
        'signature': signature,
        'orderGroupId': orderGroupId,
        # 'orderExpireTime': orderExpireTime
        
    }

    response = requests.post(endpoint, json=data, headers={'Content-Type': 'application/json'})

    return response.json()



