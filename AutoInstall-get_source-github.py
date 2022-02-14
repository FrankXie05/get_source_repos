#!/usr/bin/env python3
import sys
import requests
import os
from importlib import import_module

class AutoInstall():
    _loaded = set()

    @classmethod
    def find_spec(cls, name, path, target=None):
            if path is None and name not in cls._loaded:
                cls._loaded.add(name)
                print("Installing", name)
                try:
                    result = os.system('pip install {}'.format(name))
                    if result == 0:
                        return import_module(name)
                except Exception as e:
                    print("Failed", e)
            return None

sys.meta_path.append(AutoInstall)

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
