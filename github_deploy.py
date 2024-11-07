import os
import requests
import base64
from pathlib import Path

def get_files_content():
    excluded = {'.git', '__pycache__', '.upm', '.config', '.cache', 'venv', '.replit', 'replit.nix'}
    files = []
    
    for path in Path('.').rglob('*'):
        if (not any(x in str(path) for x in excluded) and 
            path.is_file() and 
            not path.name.startswith('.')):
            with open(path, 'rb') as f:
                content = f.read()
                files.append({
                    'path': str(path),
                    'content': base64.b64encode(content).decode('utf-8'),
                    'encoding': 'base64'
                })
    return files

def check_repository_files():
    token = os.environ['GITHUB_TOKEN']
    repo = "veterinary-ce-webinar"
    owner = "MargotBot"
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print("Repository files check successful")
        return True
    print(f"Repository files check failed: {r.status_code}")
    return False

def verify_pages_settings():
    token = os.environ['GITHUB_TOKEN']
    repo = "veterinary-ce-webinar"
    owner = "MargotBot"
    url = f"https://api.github.com/repos/{owner}/{repo}/pages"
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print("GitHub Pages settings verified")
        pages_data = r.json()
        print(f"Pages URL: {pages_data.get('html_url', 'Not available')}")
        return True
    print(f"GitHub Pages settings check failed: {r.status_code}")
    return False

def enable_github_pages(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/pages"
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        "source": {
            "branch": "main",
            "path": "/"
        }
    }
    r = requests.post(url, headers=headers, json=data)
    print(f"Enabled GitHub Pages: {r.status_code}")

def push_to_github():
    token = os.environ['GITHUB_TOKEN']
    repo = "veterinary-ce-webinar"
    owner = "MargotBot"
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    print("Starting GitHub deployment verification...")
    
    # Check repository files
    if not check_repository_files():
        print("Uploading files to repository...")
        files = get_files_content()
        for file in files:
            url = f"{base_url}/contents/{file['path']}"
            data = {
                'message': f"Add {file['path']}",
                'content': file['content']
            }
            r = requests.put(url, headers=headers, json=data)
            print(f"Uploaded {file['path']}: {r.status_code}")
    
    # Verify GitHub Pages settings
    verify_pages_settings()

if __name__ == "__main__":
    push_to_github()
