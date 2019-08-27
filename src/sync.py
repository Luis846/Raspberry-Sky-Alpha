import requests
import json
import time

def sync_data():
        r = requests.get('http://192.168.10.139:5000/platinum', stream=True)
        time.sleep(10)
        # for line in r.iter_lines():
        #     if line:
        #         print(json.loads(line))

        for line in r.iter_lines():
                if line:
                        bob = json.loads(line)
                        print(bob)