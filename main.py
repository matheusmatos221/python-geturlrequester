import requests


URL = "https://camo.githubusercontent.com/2cd9241d7e901320c866394f4b650fb829e4215f0b91970" \
      "f75b3db1bcce9682b/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d" \
      "652f6d6174686575736d61746f733232312f636f756e742e737667"
NUMBER_GET_REQUESTS = 100000

if __name__ == '__main__':
    for i in range(1, NUMBER_GET_REQUESTS + 1):
        # sending get request and saving the response as response object
        print(f'GET request number: {i}')
        r = requests.get(url=URL)
