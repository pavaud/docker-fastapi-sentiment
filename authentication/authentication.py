import os

import requests

API_ADDRESS = 'fastapi_container'
API_PORT = 8000

# users db
users = [
        ('alice', 'wonderland', 200),
        ('bob', 'builder', 200),
        ('clementine','mandarine',403)
]

for user in users:

    # request
    r = requests.get(
        url='http://{address}:{port}/permissions'.format(address=API_ADDRESS, port=API_PORT),
        params= {
            'username': user[0],
            'password': user[1]
        }
    )

    output = '''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username={username}
    | password={password}

    expected result = {expected_status}
    actual restult = {actual_status}

    ==>  {test_status}

    '''

    # request status
    status_code = r.status_code

    # display results
    if status_code == user[2]:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    output = output.format(username=user[0],
                           password=user[1],
                           expected_status=user[2],
                           actual_status=status_code,
                           test_status=test_status)
    print(output)

    # export results to file
    if os.environ.get('LOG') == '1':  
        with open('./log/api_test.log', 'a') as file:
            file.write(output)