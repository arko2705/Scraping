# import the required libraries
import requests
import itertools

# create a proxy list (create your own proxy list)
proxy_list = [
    {
        "http": "http://162.240.19.30:80",
        "https": "http://123.140.160.54:5031",
    },
    {
        "http": "http://115.74.11.235:10002",
        "https": "http://123.141.181.8:5031",
    },
    # ...
]


# define a proxy rotator using a generator
def proxy_rotator(proxy_list):
    return itertools.cycle(proxy_list)

# create a generator from the proxy rotator function
proxy_gen = proxy_rotator(proxy_list)

# rotate the proxies for three requests
for request in range(3):
    # send a request to httpbin.io
    response = requests.get("https://httpbin.io/ip", proxies=next(proxy_gen))
    # print the response text to see your current IP
    print(response.text)
