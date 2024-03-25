import ansible_runner
import requests

# run playbook
r = ansible_runner.run(playbook='/workspaces/ensf400-lab5-ansible/hello.yml')

# verify response 
response = requests.get('https://didactic-giggle-5j769rx59qqc4gj4-80.app.github.dev/')
if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to fetch URL: {response.status_code} {response.reason}")
