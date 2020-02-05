def checkSiteTemperature():
    import os
    import requests
    import lxml.html as lh
    import json

    if os.name == 'nt':  # Windows
        os.chdir('E:/oselox/projects/Include/Driver')
        print(os.getcwd())
        path = os.getcwd()
    elif os.name == 'posix':  # OSX
        print(os.getcwd)
        os.chdir('/Users/oselox/projects/Include/Driver')
        print(os.getcwd())
        path = os.getcwd()
    else: #Linux
        print(os.getcwd)
        os.chdir('/home/oselox/projects/Include/Driver')
        print(os.getcwd())
        path = os.getcwd()

    url = 'http://X.X.X.X/getData.json'
    headers = {  # headers dict to send in request
        "src": "RA",
        "_": "1580515381467"
    }
    s = requests.session()
    response = s.get(url, headers=headers)
    doc = lh.fromstring(response.content)
    res = json.loads(doc.text)
    array=[]
    print(res['sensor'][0]['tempc'])
    print(res['sensor'][1]['tempc'])

    array.append(res['sensor'][0]['tempc'])
    array.append(res['sensor'][1]['tempc'])

    return array
