#!/usr/bin/env python3
import sys
import requests

owner_and_repo = sys.argv[1]
release_url = f'https://api.github.com/repos/{owner_and_repo}/releases/latest'
headers = {'accept': 'application/vnd.github.v3+json'}
r = requests.get(release_url, headers=headers)
if len(sys.argv) == 3:
    tag_name = sys.argv[2]
else: 
    tag_name = r.json()["tag_name"]    

tag_url = f'https://api.github.com/repos/{owner_and_repo}/git/ref/tags/{tag_name}'
headers = {'accept': 'application/vnd.github.v3+json'}
r = requests.get(tag_url, headers=headers)
commit_sha = r.json()["object"]["sha"]

print(f"tag:{tag_name} commit_id:{commit_sha}")