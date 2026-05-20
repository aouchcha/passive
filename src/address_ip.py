import requests

def searchForIp(ip: str) :
    result = {"data": [], "error": None}
    URL = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as"
    response = requests.get(url=URL, timeout=2)
    if not response:
        return "Error: Could not reach IP lookup API. Check your connection."
    body = response.json()
    if body["status"] == 'fail':
        if body["message"] == "invalid query":
            message = "invalid ip address"
        else:
            message = body["message"]
        result["data"] = None
        result["error"] = message
    else:
        for k, v in body.items():
            if not k == "status":
                result["data"].append(f"{k} : {v}")
    return result