import requests
import json

pattern = [('.|.'*(2*i + 1)).center(33, '-') for i in range(5) ]
print('\n'.join(pattern + ['IP-TRACER'.center(33, '-')] + pattern[::-1]))

url = 'http://ip-api.com/json/'
ip = input('Enter IP Address : ')
r = requests.get(url+ip)
data = r.json()

print ('\nIP : ' + data['query'])
print ('Status : ' + data['status'])
print ('Region : ' + data['regionName'])
print ('City : ' + data['city'])
print ('Country : ' + data['country'])
print ('ISP : ' + data['isp'])
print ('Lat, Lon : ' + str(data['lat']) + '  ' + str(data['lon']))
print ('ZIPCODE : ' + data['zip'])
print ('Timezone : ' + data['timezone'])
print ('AS : ' + data['as'])
