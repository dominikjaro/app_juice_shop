import requests

headers = {
    'Authorization': 'Token feebebd053b74f9564ff99731d10c99edb634f9b'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'engagement': 37,
    'scan_type': 'GitLeaks Scan',
    'minimum_severity': 'Low',
    'environment': 'Test'
}

files = {
    'file': open('gitleaks.json', 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')
