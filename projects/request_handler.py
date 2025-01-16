# A program that makes requests to a public API 
# handles error for network errors and 
# invalid responses and rate limits

# Algorithm
# import requests library to handle requests
# import time library
# create a func to fech data from the public API and handles exceptions
# set your max retry num and retry delay
# create a for loop to iterate over the max retries set 
# create a try and catch exception block 
# make the get request
# ---------------Finish the algorithm-----------------------


import requests
import time

def get_request_data(url) :
    max_retries = 3
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try :
            response = requests.get(url)

            # check if request was successful
            if response.status_code == 200:
                data = response.json()
                print(f"Your request was successful. your data: {data}")
                return data

            # handle request limiting
            elif response.status_code == 429 :
                print("Rate limit exceeded. Retrying in a moment...")
                time.sleep(retry_delay)
            
            # handle other http errors
            else :
                print(f"Unexpected status code: {response.status_code}. Response: {response.text}")
                break # exit the retry loop

        except requests.exceptions.RequestException as e : 
            print(f"Network error: {e}")
            break

    print("Failed to fetch data after multiple attempts ")
    return

# Fetching data from jsonplaceholder dummy api
if __name__ == "__main__":
    api_url = "http://jsonplaceholder.typicode.com/posts/1"
    data = get_request_data(api_url)

    if data : 
        print("Data fetched successfully.")
    else:
        print("No data was fetched.")