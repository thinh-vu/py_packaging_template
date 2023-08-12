import shutil
import os
import subprocess
import requests
from trafilatura import fetch_url, extract
import yaml

# Working with file systems
def lmt_detect():
    """Detect the running OS and return file path delimiter"""
    if os.name == 'nt':
        lmt = '\\'
    else:
        lmt = '/'
    return lmt

ROOT_DIR = os.path.abspath(os.curdir)
LMT = lmt_detect()

def file_ls(directory=ROOT_DIR):
    """List all file in the root directory"""
    data = []
    for entry in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, entry)):
            data.append(entry)
    return data

def subdir_ls(basepath=ROOT_DIR):
    """List all subdirectories in the root folder"""
    data = []
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(basepath, entry)):
            data.append(entry)
    return data

def newest_file(path=ROOT_DIR):
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    return max(paths, key=os.path.getctime)

# Credentials reading
def yaml_cred(item_name, cred_path):
    """Read YAML config file"""
    with open(cred_path) as file: 
        documents = yaml.full_load(file)
        for item, doc in documents.items():
            if item == item_name:
                return doc

# run cmd commands
def env_setup(command_ls):
    """Run the cmd command. Use the pipe `|` to separate each command"""
    os.system(command_ls)

def runcmd(cmd, verbose = False, *args, **kwargs):
    """Run cmd commands"""
    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

# Data loading
def read_txt(path_to_file):
    """Read a plain text file"""
    with open(path_to_file) as f:
        content = f.read()
    return content

# Memory cleaning
def memory_cleaner():
    """Free up memory from large model data"""
    import gc
    import torch
    gc.collect()
    torch.cuda.empty_cache()


# API Request
def api_request(url, payload={}, method='GET'):
    """Request any API endpoints with a default User-Agent"""
    headers = {
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-platform': '"macOS"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
    response = requests.request(f"{method}", url, headers=headers, data=payload)
    return response.json()

# Get Google font
def get_google_font(font_family):
    """Download & extract a Google font to local folder"""
    lmt = lmt_detect()
    font_url = 'https://fonts.google.com/download?family={}'.format(font_family)
    response = requests.get(font_url)
    file_name = ROOT_DIR + lmt + '{}.zip'.format(font_family)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    shutil.unpack_archive(file_name, lmt.join([ROOT_DIR, 'font', font_family]))

# Convert Web to text
def web_to_text(url):
    downloaded = fetch_url(url)
    result = extract(downloaded)
    return result
