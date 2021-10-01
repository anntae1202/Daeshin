from flask import Flask
from flask_restx import Api, Resource, reqparse
import cx_Oracle as cx
import os
import sys
import json
from flask import jsonify, make_response, render_template, request, url_for
import base64
from werkzeug.utils import redirect

def init_session(connection, requestedTag_ignored):
    cursor = connection.cursor()
    
    
def start_pool():
    pool_min= 6 # 밑에 api 갯수같음.
    pool_max = 6 # 위와 동일
    pool_inc=0
    pool_gmd=cx.SessionPool(uesr="접속아이디",
                           password="비번",
                           dsn="데이터베이스 이름", # tnsname.ora확인하기
                           min=pool_min,
                           max=pool_max,
                            increment=pool_gmd,
                            sessionCallback=init_session)
    return pool
    
    
sql = "select 컬럼명 from 데이터이름 where 조건"

app=Flask(__name__)
app.config['JSON_AS_ASCII']=False
api=Api(app)


@api.route('/hello1')
class helloworld(Resource):
    def get(self):
        connection=pool.acquire()
        cursor = connection.cursor()
        cursor.execute("select 컬럼명 from 데이터이름 where 조건")
        r=cursor.fetchone()
        
        return jsonify({'hello' : r})
        
@api.route('/hello2')
class helloworld(Resource):
    def get(self):
        connection=pool.acquire()
        cursor = connection.cursor()
        cursor.execute("select 컬럼명 from 데이터이름 where 조건")
        r=cursor.fetchone()
        
        return jsonify({'hello' : r})        
        
        
@api.route('/hello3')
class helloworld(Resource):
    def get(self):
        connection=pool.acquire()
        cursor = connection.cursor()
        cursor.execute("select 컬럼명 from 데이터이름 where 조건")
        r=cursor.fetchone()
        
        return jsonify({'hello' : r})        
        
@api.route('/hello4')
class helloworld(Resource):
    def get(self):
        connection=pool.acquire()
        cursor = connection.cursor()
        cursor.execute("select 컬럼명 from 데이터이름 where 조건")
        r=cursor.fetchone()
        
        return jsonify({'hello' : r})
        
        
@api.route('/hello5')
class helloworld(Resource): # 이미지 파일을 인코딩시켜서 리턴
    def get(self):
        with open('logo.png', 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_message = base64_encoded_data.decode('utf-8')

            return base64_message
        # json형식으로 뽑을거면
#             image = {
#                 "image" : base64_message
#                     }
#             return image
        
        
class index(Resource):
    def get(self):
        try:
            parser=reqparse.RequestParser()
            parser.add_argument('x', required = True, type=str , help="not enough..")
#             parser.add_argument('y', required = True, type=int , help="not enough..")
            args=parser.parse_args()
            result = {'id' : args['x']}
            return jsonify(result)
        
        except Exception as e:
            return jsonify({'error' : str(result)})
api.add_resource(index, "/hello6")
# /hello6?x=대신증권 이렇게 입력하기


if __name__ == "__main__":
    # strat a pool of connection
    pool = start_pool()
    app.run(debug=True, host='hostnumber', port=port)
    # app.run(host='hostnumber', port= 'port', debug=True, use_reloader=False)
    
    
    
    
