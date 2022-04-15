import requests
import json
def api():
    url=requests.get("http://saral.navgurukul.org/api/courses")
    with open("courses.json","w")as file:
        dic=json.loads(url.text)
        json.dump(dic,file,indent=4)
        print(dic)
api()


