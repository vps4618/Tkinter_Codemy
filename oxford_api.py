import requests
import json
app_id = "291c736c"
app_key = "c83cdf52e3e9151b0e97c03d13aad164"
language = "en-gb"
word_id = "girl"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
r = requests.get(url, headers={"app_id":app_id, "app_key":app_key})
result=json.loads(r.content)
#print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])
#print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'])
#print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'])
#print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['shortDefinitions'])
#print(result['results'][0]['lexicalEntries'][1]['phrases'])

length=len(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['examples'])
for i in range(length):
    print(result['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['examples'][i]['text'])
list=[1,2,3]
print(len(list))