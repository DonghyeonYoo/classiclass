import requests

API_BASE_URL = "http://api.openapi.io/ppurio/{API_VERSION}/message/sms/{CLIENT_ID}".format(
    API_VERSION=1,
    CLIENT_ID='dobestan',
)


def send_sms(send_phone, dest_phone, msg_body):
    response = requests.post(
        API_BASE_URL,
        data={
            'send_phone': send_phone,
            'dest_phone': dest_phone,
            "msg_body": msg_body,

        },
        headers={
            "x-waple-authorization": "MTkyMC0xNDEzODU0NTAwMzU3LTllM2VkOTM3LTYwMTEtNGU2Zi1iZWQ5LTM3NjAxMTNlNmYyMg==",
        }
    )
    return response
