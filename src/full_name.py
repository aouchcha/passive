import requests

def fullName(fullName: str):
    result = {"data":[], "error":None}
    sli = fullName.split(" ")
    if not len(sli) == 2:
        result["error"] = "Error: Usage 'firstName lastName'"
        result["data"] = None
        return  
    firstName = sli[0]
    lastName = sli[1]
    URL = f"https://api.hunter.io/v2/email-finder?domain=linkedin.com&first_name={firstName}&last_name={lastName}&api_key=d91eed521bd2e3ae4693ad653905ed3edeb52b2d"
    response = requests.get(url=URL, timeout=5)
    body = response.json()
    print(body)
    return result