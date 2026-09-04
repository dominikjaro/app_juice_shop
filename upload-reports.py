import requests
import sys

file_name = sys.argv[1]
scan_type = ""

if file_name == "gitleaks.json":
    scan_type = "Gitleaks Scan"
elif file_name == "njsscan.sarif":
    scan_type = "SARIF"
elif file_name == "semgrep.json":
    scan_type = "Semgrep JSON Report"
elif file_name == "retire.json":
    scan_type = "Retire.js Scan"
elif file_name == "trivy.json":
    scan_type = "Trivy Scan"

headers = {
    'Authorization': 'Token 2a57562bf544ffadef11d8cb8b31d70fc7314917'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'engagement': 31,
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
