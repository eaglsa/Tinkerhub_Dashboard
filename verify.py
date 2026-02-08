import requests
try:
    response = requests.get("http://127.0.0.1:8000/")
    if "alice.sh" in response.text and "0xbob" in response.text:
        print("SUCCESS: Found expected tech aliases.")
    else:
        print("FAILURE: Did not find expected tech aliases.")
    if "import antigravity" in response.text:
         print("SUCCESS: Found easter egg.")
except Exception as e:
    print(e)
