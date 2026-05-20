import requests
import json

def searchWithUsername(username: str):
    username = username.lstrip("@")
    result = {"data":[], "error":None}

    SOCIAL_NETWORKS = {
        "GitHub": {
            "type": "api",
            "url": f"https://api.github.com/users/{username}",
            "confirmedStatus": True
        },
        "Reddit": {
            "type": "api",
            "url": f"https://www.reddit.com/user/{username}/about.json",
            "confirmedStatus": True
        },
        "GitLab": {
            "type": "api",
            "url": f"https://gitlab.com/api/v4/users?username={username}",
            "confirmedStatus": False
        },
        "StackOverflow": {
            "type": "api",
            "url": f"https://api.stackexchange.com/2.3/users?inname={username}&site=stackoverflow",
            "confirmedStatus": False
        },
        "YouTube": {
            "type": "api",
            "url": f"https://www.youtube.com/@{username}",
            "confirmedStatus": True
        },
        "TikTok": {
            "type": "api",
            "url" : f"https://www.tikvib.com/profile/{username}",
            "confirmedStatus": True
        },
        "Twitter": {
            "type": "api",
            "url": f"https://nitter.net/{username}",
            "confirmedStatus": True
        }
    }

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
    }

    POSITIVE_STATUS = {200, 301, 302}

    for platform, obj in SOCIAL_NETWORKS.items():
        url = obj["url"]
        isConfirmed = obj["confirmedStatus"]
        response = requests.get(url, allow_redirects=True, timeout=2, headers=HEADERS)
        if response.status_code in POSITIVE_STATUS and isConfirmed:
            result["data"].append(f"{platform} : yes")
        elif response.status_code in POSITIVE_STATUS:
            try:    
                body = response.json()
                if platform == "GitLab":
                    result["data"].append(f"{platform} : {'yes' if Gitlab(body) else 'no'}")
                else:
                    result["data"].append(f"{platform} : {'yes' if StackOverFlow(body) else 'no'}")
            except json.decoder.JSONDecodeError:
                result["data"].append(f"{platform} : no")
        else:
            result["data"].append(f"{platform} : no")
    return result


def Gitlab(body):
    return len(body) > 0

def StackOverFlow(body):
    return len(body["items"]) > 0