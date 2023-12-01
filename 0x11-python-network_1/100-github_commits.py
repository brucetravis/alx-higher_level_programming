#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 3:
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f'{sha}: {author_name}')
    else:
        print(f"Error: {response.status_code}")
else:
    print("Usage: ./100-github_commits.py <repo_name> <owner_name>")
