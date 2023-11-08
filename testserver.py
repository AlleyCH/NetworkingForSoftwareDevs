# import urllib
from flask import Flask, request
import gzip, random

# users = {
#     'arben': {
#         'fname': 'Arben',
#         'lname': 'Tapia',
#         'age': 56,
#         'courses' : ['COMP253','COMP305', 'COMP395']
#     },
#     'narendra': {
#         'fname': 'Narendra',
#         'lname': 'Pershad',
#         'age': 45,
#         'courses' : ['COMP100', 'COMP123', 'COMP216']

#     },
#     'hao': {
#         'fname': 'Hao',
#         'lname': 'Lac',
#         'age': 40,
#         'courses' : ['COMP231','COMP228']
#     }
# }

app = Flask(__name__)

@app.route('/ques6a', methods=['GET'])
def show_query_string():
    '''
    Returns the arguments that was sent by the request<br/>[browser sup only if query string supplied]
    '''
    return request.args


@app.route('/ques6b', methods=['POST'])
def show_form_data():
    '''
    Returns the arguments that was sent by the request<br/>[browser sup only if query string supplied]
    '''
    return request.form

@app.route('/ques6c')
def show_user_agent():
    '''
    Returns all the users in the collection<br/>[browser sup]
    '''
    return str(request.user_agent)

@app.route('/ques6d', methods=['GET', 'POST'])
def compress_content():
    '''
    Sends compressed content to the client.

    '''
    data = b'Networking for Software Developers is the best course!!!'
    # return gzip.compress(bytes(data.__str__(), 'utf8'))
    return gzip.compress(data)

@app.route('/ques6e', methods=['GET', 'POST'])
def decompress_content():
    '''
    Sends un-compressed content to the client.

    '''
    print(f'{request.data}')
    if request.data == b'':
        return 'You need to send compress data to the server'
    
    return  gzip.decompress(request.data).decode("utf-8")

if __name__ == '__main__':
	app.run(debug=True)      #app.run(host, port, debug, options)