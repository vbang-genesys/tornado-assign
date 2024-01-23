""""

Server details:
-> Tornado Server
-> Database / file system
-> Data preprocessing (clean, fill null)
-> Replace print with logging
-> Add comments and docstrings wherever necessary
-> Apply Black formating to all files 

"""

import asyncio
import httpx
import logging

logging.basicConfig(
    filename="client_log.log",
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    level=logging.DEBUG,
)


async def send_request(client, method, url, data=None):
    """
    Post -> post data to url
    Get -> get data from url (url contains the clien_id)
    Return the response from the server
    """
    if method == "POST":
        response = await client.post(url, json=data)
    elif method == "GET":
        response = await client.get(url)

    return response


async def main():
    """
    -> send the json data using post
    -> receive the stored data from the server by sending the client_id
    """
    url = "http://localhost:8888"
    data = {
        "name": "Vidoosh",
        "age": "70",
        "industry": "publiccvb",
        "salary": "50",
        "city": "Chennai",
    }

    async with httpx.AsyncClient() as client:
        tasks = [send_request(client, "POST", url, data) for _ in range(2)]
        post_responses = await asyncio.gather(*tasks)
        for i, post_response in enumerate(post_responses, start=1):
            print(f"Response {i}: {post_response.text}")
        get_tasks = [
            send_request(client, "GET", url + f"?c_id={post_responze.text}")
            for post_responze in post_responses
        ]
        get_responses = await asyncio.gather(*get_tasks)
        for i, get_response in enumerate(get_responses, start=1):
            print(f"Response {i}: {get_response.text}")
        # c_id = input("Enter c_id: ")
        # task = [send_request(client, "GET", url + f"?c_id={c_id}")]
        # response = await asyncio.gather(*task)
        # print(response[0].text)


if __name__ == "__main__":
    asyncio.run(main())
