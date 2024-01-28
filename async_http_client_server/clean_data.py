"""
-> Check city
-> Add currency
-> Name format
"""

import re

def clean(data):
    """
    -> city in [Paris, Chennai, New York, Dhaka, Budapest, Tokyo, Sydney]
    -> currency in [EURO, INR, USD, BDT, HUF, JPY, AU]
    -> Returns cleaned data
    """
    city = {
        "Paris": "EUR",
        "Chennai": "INR",
        "New York": "USD",
        "Dhaka": "BDT",
        "Budapest": "HUF",
        "Tokyo": "JPY",
        "Sydney": "AUD",
    }

    if data["city"] not in city:
        return "bad request"

    data["salary"] = clean_salary(city, data["city"], data["salary"])

    data["name"] = data["name"].title()

    return data


def clean_salary(cities, city, salary):
    
    pattern = re.compile("^([A-Z]{3}\s?[0-9]+)$")

    if not pattern.match(salary):
        salary = cities[city] + salary

    else:
        if salary[:3] != cities[city]:
            salary = currency_conversion(cities, city, salary)
    
    return salary


def currency_conversion(cities, city, amount):

    """
    AUD -> USD -> INR
    1.52    1      83
    """
    
    rate_to_usd = {
        "INR": 83.12,
        "EUR": 0.92,
        "USD": 1,
        "BDT": 109.85,
        "HUF": 357.02,
        "JPY": 148.06,
        "AUD": 1.52,
    }

    temp = (float(amount[3:]) / rate_to_usd[amount[:3]]) * rate_to_usd[cities[city]]

    amount = cities[city] + str(temp)

    return amount