import os

import requests

API_ADDRESS = 'fastapi_container'
API_PORT = 8000

users = [
        ('alice', 'wonderland', (200, 200) ),
        ('bob', 'builder', (200, 403))
]

versions = ['v1','v2']

for user in users:
    for i, version in enumerate(versions):
    
        # request
        r = requests.get(
            url='http://{address}:{port}/{version}/sentiment'.format(address=API_ADDRESS, port=API_PORT,version=version),
            params= {
            'username': user[0],
            'password': user[1],
            'sentence':'fake sentence'
            }
        )

        output = '''
        ============================
            Authorization test
        ============================

        request done at "/{version}/sentiment"
        | username={username}
        | password={password}

        expected result = {expected_status}
        actual restult = {actual_status}

        ==>  {test_status}

        '''


        # request status
        status_code = r.status_code

        # display results
        if status_code == user[2][i]:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'

        output = output.format(version=version,
                               username=user[0],
                               password=user[1],
                               expected_status=user[2][i],
                               actual_status=status_code,
                               test_status=test_status)
        print(output)

        # export results to file
        if os.environ.get('LOG') == '1':
            with open('./log/api_test.log', 'a') as file:
                file.write(output)