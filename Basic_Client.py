# Alley Chaggar 

import requests

URL = 'http://127.0.0.1:5000'
response = requests.get(URL)
print(response.text)





# Alley Chaggar 
import gzip
import requests

server_ip = 'server_ip'
flask_port = 'flask_port'

URL = '«server_ip»:«flask_port»/ques6d'

response = requests.get(URL)

status_code = response.status_code

if status_code == 200:
    # Decompress the content
    compressed_content = response.content
    decompressed_content = gzip.decompress(compressed_content)

    # Decode the result
    decoded_result = decompressed_content.decode('utf-8')

    print(f'URL {URL}')