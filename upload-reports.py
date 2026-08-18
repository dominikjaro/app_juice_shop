import requests
import sys

file_name = sys.argv[1]
scan_type = ""

if file_name == "gitleaks.json":
    scan_type = "GitLeaks Scan"
elif file_name == "njsscan.sarif":
    scan_type = "SARIF"
elif file_name == "semgrep.json":
    scan_type = "Semgrep JSON Report"

headers = {
    'Authorization': 'Token feebebd053b74f9564ff99731d10c99edb634f9b'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'engagement': 37,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'environment': 'Test'
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')
