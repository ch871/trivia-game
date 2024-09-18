import requests


def get_trivia():
    url = f"https://opentdb.com/api.php?amount=20"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return "trivia not found"
    else:
        return f"Error {response.status_code}: {response.text}"


def get_users():
    url = f"https://randomuser.me/api?results=4"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return "trivia not found"
    else:
        return f"Error {response.status_code}: {response.text}"
