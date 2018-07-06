# -*- coding: utf-8 -*-

from flask import Flask, request
import json
import requests
app = Flask(__name__)
@app.route('/')
def index():
  return '{"nodes":[{"node_type":"node","nodeResponse":{"type":"text","response":"Your data "}}]}'

@app.route('/hello/<string:names>')
def home(names):
  return ("<h1>Hello %s!! </h1>" % names)


@app.route('/postjson' , methods=['POST','GET'])
def postjson():
  print (request)
  print (request.headers) 
  print (request.data)
  print ("AAA",request.form['key1'])
  print ("BBB",request.form['key2'])
  json_line = request.get_json()
  json_line = json.dumps(json_line)
  decoded = json.loads(json_line)
  #id=[d['replyToken'] for d in user][0]

  json_line = json.dumps(json_line)
  print(json_line)

  msg = {"nodes":[{"node_type":"node","nodeResponse":{"type":"text","response":"Your data "}}]} 
  json_line = json.dumps(msg)
  print (json_line) 
  print("___") 

  return ( json_line )

@app.route('/sendapi' )
def sendApi():
  print('--------------------------------------------------')
  TEST_API = 'https://chat.pt.co.th/api/json'
  headers = {
  'Content-Type': 'application/json; charset=UTF-8'
  }
  data =  "replyToken test"
  print("ข้อมูล：",data)
  print('--------------------------------------------------')
  r = requests.post(TEST_API, headers=headers, data=data) 
  print (r.text)
  return ("<h1>Hello test </h1>" )

@app.route('/callback', methods=['POST'])
def callback():
  json_line = request.get_json()
  json_line = json.dumps(json_line)
  decoded = json.loads(json_line)
  user = decoded["events"][0]['replyToken']

  print(json_line)
  print("ผู้ใช้：",user)
  print('ทดสอบ') 
  sendText(user,'สวัสดีค่ะ') 
  symbol = 'PTT'       
  return '',200


def sendText(user, text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer 6nM7I+2cxCF+BC+4HCEjqglxt4SXejOEqxw60Tocc7f9+ZfGuoYbRBJbuC+wEkhWI6Ej3kxMpbehs6V6Uxx4YKNN9v1yqklxgpDpp6fuT+W2jcoEYL7pux7CfnHWC35vrSd6MqbSgWS8JpZ1K3LXaQdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization':Authorization
  }
  data = json.dumps({
  "replyToken":user,
  "messages":[{"type":"text","text":text}]})
  print("ข้อมูล：",data)
  r = requests.post(LINE_API, headers=headers, data=data) 


if __name__ == '__main__':
  app.run(debug=True)