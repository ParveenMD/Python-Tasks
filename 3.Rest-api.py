print("MD Parveen")
import requests
result = requests.get("http://api.open-notify.org/astros.json")
get_data=result.json()
print(get_data)