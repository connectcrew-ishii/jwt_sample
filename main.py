# -*- coding: utf-8 -*-

from boxsdk import JWTAuth, Client
import os

auth = JWTAuth(
    client_id=os.environ["clientID"],
    client_secret=os.environ["clientSecret"],
    enterprise_id=os.environ["enterpriseID"],
    jwt_key_id=os.environ["publickeyID"],
    rsa_private_key_data=os.environ['privateKey'],
    rsa_private_key_passphrase=b'047dac7e6cd83f6b2a858014b50feb40',
)

access_token = auth.authenticate_instance()
print(access_token)

"""
# 認証
auth = JWTAuth(
        client_id=os.environ["clientID"],
        client_secret=os.environ["clientSecret"],
        enterprise_id=os.environ["enterpriseID"],
        jwt_key_id="nno2ipwo",
        )
client = Client(auth)
user = client.user().get()
print('The current user ID is {0}'.format(user.id))

 
# ユーザ権限移譲
user_to_impersonate = client.user(user_id = "3056900391")
user_client = client.as_user(user_to_impersonate)

 
# ファイルの情報取得
fileResponse = user_client.file("514033811180").get_items(limit=5)
print(fileResponse)
"""
