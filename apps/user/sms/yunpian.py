from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
import random


def random_num():
    string = ""
    for i in range(6):
        num = chr(random.randrange(ord('0'), ord('9') + 1))
        string += num
    return string


def sms(phone):
    code = random_num()
    clnt = YunpianClient('2ea27e4b949fa2ab4b5da4b80702c303')
    param = {YC.MOBILE: phone, YC.TEXT: '您的验证码是{}。如非本人操作，请忽略本短信'.format(code)}
    r = clnt.sms().single_send(param)
    return [r.code(), code]
