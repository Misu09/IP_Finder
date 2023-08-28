import requests
from ipwhois import IPWhois
from unidecode import unidecode

def get_ip_info(ip_address):
    # Get IP information using ipinfo.io API
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    
    country = data.get("country", "N/A")
    region = str(data.get("region", "N/A"))
    city = str(data.get("city", "N/A"))
    asn = str(data.get("asn", {}).get("asn", "N/A"))
    isp = str(data.get("asn", {}).get("name", "N/A"))

    # If ipinfo.io does not have ISP information, use WHOIS
    obj = IPWhois(ip_address)
    results = obj.lookup_rdap()
    if country == "N/A":
        country = str(results.get("asn_country_code", "N/A"))
    if region == "N/A":
        region = str(results.get("asn_region", "N/A"))
    if city == "N/A":
        city = str(results.get("asn_city", "N/A"))        
    if asn == "N/A":
        asn = str(results.get("asn", "N/A"))
    if isp == "N/A":
        isp = str(results.get("asn_description", "N/A"))

    return country, region, city, asn, isp
    
if __name__ == "__main__":
    ip_list = [
        # Add the rest of your IP addresses here
        "194.209.2.56",
        "198.217.129.227",
        "84.94.81.79",
        "117.239.8.127"
    ]

    with open('results.txt', 'w') as f: 
        for ip_address in ip_list:
            country, region, city, asn, isp = get_ip_info(ip_address)
            print(f"IP: {unidecode(ip_address)}\tCountry: {unidecode(country)}\tRegion: {unidecode(region)}\tCity: {unidecode(city)}\tASN: {asn}\tISP: {unidecode(isp)}")
            f.write(f"{country},{region},{city},{asn},{isp}\n")
