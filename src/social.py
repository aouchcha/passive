import requests

def searchWithUsername(username: str):
    username = username.lstrip("@")
    result = {"data":[], "error":None}

    SOCIAL_NETWORKS = {
        "GitHub":           f"https://api.github.com/users/{username}",
        "Reddit":           f"https://www.reddit.com/user/{username}/about.json",
        "GitLab":           f"https://gitlab.com/api/v4/users?username={username}",
        "StackOverflow":    f"https://api.stackexchange.com/2.3/users?inname={username}&site=stackoverflow",
        "Bitbucket":        f"https://api.bitbucket.org/2.0/users/{username}",
        "YouTube"   :       f"https://www.youtube.com/user/{username}",
        "Instagram":        f"https://www.instagram.com/{username}/",
        "TikTok":           f"https://www.tiktok.com/@{username}"
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

    for platform, url in SOCIAL_NETWORKS.items():
        response = requests.get(url=url, headers=HEADERS, allow_redirects=True, timeout=5)
        if response.status_code in POSITIVE_STATUS:
            body = response.json()
            print(f"{platform}     {body}")
            if platform == "GitLab":
                if len(body) > 0 : 
                    exist = "yes" 
                else:
                    exist = "no"
            else: 
                exist = "yes"
        else:
            exist = "no"            
        result["data"].append(f"{platform} : {exist}")
    print(result["data"])
