import json

def clean():
    """
    -> city in [Paris, Chennai, New York, Dhaka, Budapest, Tokyo, Sydney]
    -> currency in [EURO, INR, USD, BDT, HUF, JPY, AU]
    """
    with open('async_http_client_server/client_responses.json', 'r+') as f:
        data = json.load(f)
        city = {
            "Paris": "EURO", 
            "Chennai": "INR", 
            "New York": "USD", 
            "Dhaka": "BDT", 
            "Budapest": "HUF", 
            "Tokyo": "JPY", 
            "Sydney": "AU"}
        for d in data:
            d["salary"] = city[str(d["city"])] + d["salary"]
            print(d["salary"])


        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

if __name__ == "__main__":
    clean()