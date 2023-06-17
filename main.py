import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import pycountry

print('-----------------------------------------')
in_num = input('Please enter a phone number: ')
print('-----------------------------------------')
try:
   num = phonenumbers.parse(in_num)
except phonenumbers.NumberParseException:
    print("Invalid phone number")
    exit()
region_code = phonenumbers.region_code_for_country_code(num.country_code)
provider = carrier.name_for_number(num, region_code)
timeZone = timezone.time_zones_for_number(num)
region = geocoder.description_for_number(num,"en")
country = pycountry.countries.get(alpha_2=region_code)

print("[+]", num)
print("[+] Service provider: "+ provider)
print("[+] Timezone: "+ str(timeZone))
print("[+] Country: "+ region)

print('-----------------------------------------')

