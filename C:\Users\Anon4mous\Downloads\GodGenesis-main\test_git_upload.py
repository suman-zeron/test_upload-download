'''
import os
from github import Github
def download_file(file_name):
    #x=os.getcwd()
    filepath=file_name
    
    GITHUB_REPO="test_upload-download"

    g = Github("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")

    repo = g.get_user().get_repo(GITHUB_REPO)
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

    with open(filepath, 'rb') as file:
        content = file.read()

    git_prefix = 'folder1/'
    git_file = filepath
    repo.create_file(git_file, "extracted files", content, branch="main")
    print(git_file + ' CREATED')

se=input("Enter the path:")

download_file(se)
'''

import requests
url="https://github.com/GodGenesis/test_upload-download/blob/main/C:/Users/Anon4mous/Downloads/GodGenesis-main/suman_cv_IEM_ish.pdf"
r=requests.get(url,allow_redirects=True)
