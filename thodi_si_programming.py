import requests
import json
url=requests.get("http://saral.navgurukul.org/api/courses")
with open("courses.json","w")as file:
    dic=json.loads(url.text)
    json.dump(dic,file,indent=4)
course=int(input("enter any course no."))
if course in dic:
    print(dic,course)