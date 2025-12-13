import requests
response = requests.get("https://tulsu.ru/schedule/queries/GetSchedule.php?search_field=GROUP_P&search_value=220032-11")
print(response.json()[:2])