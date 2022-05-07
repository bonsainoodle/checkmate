import requests as req
import json


def email_in_endpoint(url, email) -> bool:
    r = req.post(url, json={"email": email})
    if r.status_code == 200:
        return True
    else:
        return False


def add_user(url, email, discordId) -> bool:
    r = req.post(url, json={"email": email, "discordId": discordId})
    if r.status_code == 201:
        return True
    else:
        return False
