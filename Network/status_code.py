import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.148 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9 '
}

url = 'https://url.dns.com'

print(f'Initial address: {url}')

req = requests.head(url=url, headers=headers)

redirect = None
if req.status_code == 301:
    print(f'Server response: {req.status_code}')
    try:
        redirect = req.headers['Location']
        print(redirect)
        print(f'Redirect: {redirect}')
        req = requests.get(url=redirect, headers=headers)
        print(f'Server response: {req.status_code}')
    except KeyError:
        print('There is no redirect address')

print(f'Server response: {req.status_code}')
