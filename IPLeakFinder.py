import sys
import ssl
import urllib3   #python3 -m pip install --upgrade --user urllib3==1.26.15   (If you need to upgrade your urllib3)
import requests  #sudo pip3 install --upgrade requests 
import argparse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from http.client import HTTPConnection
HTTPConnection._http_vsn_str = 'HTTP/1.0'    #Force send HTTP/1.0

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def parse_args():
    parser = argparse.ArgumentParser(description='Internal IP Disclosure Scanner')
    parser.add_argument('-f', '--file', required=True, help='File containing list of IPs to scan')
    parser.add_argument('-p', '--proxy', help='Proxy URL (e.g., http://127.0.0.1:8080)')
    return parser.parse_args()

def main():
    args = parse_args()
    
    proxies = None
    if args.proxy:
        proxies = {
            "http": args.proxy,
            "https": args.proxy
        }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
        'Host': urllib3.util.SKIP_HEADER,  #Skips sending a Host header altogether
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'close'
    }

    with open(args.file) as f:
        IPs = f.read().splitlines()

    for targets in IPs:
        try:
            request_kwargs = {
                'verify': False,
                'headers': headers,
                'allow_redirects': False,
                'timeout': 5
            }
            if proxies:
                request_kwargs['proxies'] = proxies
                
            response = requests.get("https://" + str(targets), **request_kwargs)
            if response.status_code == 302:
                print(f"{GREEN}{str(targets)} ---- Vulnerable: Internal Location: {response.headers['Location']}{RESET}")
        except:
            print(f"{RED}{str(targets)} ---- Not Vulnerable{RESET}")

if __name__ == "__main__":
    main()
        
    
