# 这里有一个点需要说明一下，return data
# 这个data最好采用dict的形式返回，这样在以后接口扩展时可以更好的支持
import ujson as json
import urllib.parse
from flask import request
from api import Api
from api import errors
from . import controllers as account_ctl
from gt import session
from gt import redis
from flask import current_app


class Login(Api):
    NEED_LOGIN = False

    def get(self):
        pass

    def post(self):
        pass


class Token(Api):
    NEED_LOGIN = False

    def get(self):
        token = redis.client.get('token')
        openid = redis.client.get('openid')
        if token and openid:
            token = token.decode()
            openid = openid.decode()
        else:
            token = ''
            openid = ''
        data = {
            'token': token,
            'openid': openid,
        }
        return data

    def post(self):
        data = request.data
        current_app.logger.info(data)
        data = data.decode()
        current_app.logger.info(data)
        data = urllib.parse.unquote(data)
        current_app.logger.info(data)
        data = json.loads(data)
        openid = data.get('openid')
        token = data.get('token')
        redis.client.set('token', token)
        if openid:
            redis.client.set('openid', openid)
