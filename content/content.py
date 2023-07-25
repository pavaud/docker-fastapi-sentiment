import os
import json

import requests


API_ADDRESS = 'fastapi_container'
API_PORT = 8000

sentences = [("life is beautiful","positif"),("that sucks","negatif")]
versions = ['v1','v2']

for version in versions:
    for i, sentence in enumerate(sentences):
    
        # request
        r = requests.get(
            url='http://{address}:{port}/{version}/sentiment'.format(address=API_ADDRESS, port=API_PORT,version=version),
            params= {
                'username': 'alice',
                'password': 'wonderland',
                'sentence':sentence[0]
            }
        )

        output = '''
        ============================
            Content test
        ============================

        request done at "/{version}/sentiment"
        | username=alice
        | password=wonderland

        expected result = {expected_score}
        actual restult = {actual_score}

        ==>  {test_status}

        '''

        # request status
        status_code = r.status_code
        
        # score
        score = json.loads(r.text)['score']

        # display results
        if status_code == 200 and \
            ((i == 0 and score > 0) or \
                (i == 1 and score < 0)):
            test_status = 'SUCCESS'   
        else:
            test_status = 'FAILURE'

        output = output.format(version=version,
                               expected_score=sentence[1],
                               actual_score=score,
                               status_code=status_code, 
                               test_status=test_status)
        print(output)

        # export results to file
        if os.environ.get('LOG') == '1':
            with open('./log/api_test.log', 'a') as file:
                file.write(output)