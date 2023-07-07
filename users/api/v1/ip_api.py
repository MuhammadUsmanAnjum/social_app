import requests
import holidays


def get_country_from_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()
    return data["countryCode"]

  
def is_holiday(country, date):
    country_holidays = holidays.CountryHoliday(country)  # Replace 2023 with the desired year
    if date in country_holidays:
        return True
    else:
        return False

def get_wan_ip(): 
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    wan_ip = data['ip']
    return wan_ip


