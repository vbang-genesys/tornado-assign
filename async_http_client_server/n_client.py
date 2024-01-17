import asyncio
import httpx

async def send_request(client, method, url, data=None):
    
    if method == "GET":
        response = await client.get(url)
    elif method == "POST":
        response = await client.post(url, json=data)
    
    return response
        
async def main():
    url = "http://localhost:8888"
    data = {
        "name" : "Vidoosh",
        "age" : "70",
        "industry" : "publiccvb",
        "salary" : "50",
        "city" : "Chennai"        
    }

    async with httpx.AsyncClient() as client:
        tasks = [send_request(client, "POST", url, data) for _ in range(800)] + [send_request(client, "GET", url + f"?name=User{i}&age={20+i}") for i in range(800)]
        responses = await asyncio.gather(*tasks)
        for i, response in enumerate(responses, start=1):
            print(f"Response {i}: {response.text}")

if __name__ == "__main__":
    asyncio.run(main())