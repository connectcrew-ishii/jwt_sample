# -*- coding: utf-8 -*-
# import urllib.request
# print(urllib.request.getproxies())


from boxsdk import JWTAuth, Client
import os

# 認証
auth = JWTAuth(
        client_id=os.environ["clientID"],
        client_secret=os.environ["clientSecret"],
        enterprise_id=os.environ["enterpriseID"],
        jwt_key_id=os.environ["publicKeyID"],
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
