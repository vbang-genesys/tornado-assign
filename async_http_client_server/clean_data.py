"""
-> Check city
-> Add currency
-> Name format
"""

import json


def clean(data):
    """
    -> city in [Paris, Chennai, New York, Dhaka, Budapest, Tokyo, Sydney]
    -> currency in [EURO, INR, USD, BDT, HUF, JPY, AU]
    -> Returns cleaned data
    """
    city = {
        "Paris": "EURO",
        "Chennai": "INR",
        "New York": "USD",
        "Dhaka": "BDT",
        "Budapest": "HUF",
        "Tokyo": "JPY",
        "Sydney": "AU",
    }

    if data["city"] not in city:
        return "bad request"

    data["salary"] = city[str(data["city"])] + data["salary"]
    data["name"] = data["name"].title()

    return data
