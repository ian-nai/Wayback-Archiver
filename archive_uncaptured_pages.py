import savepagenow
import requests

url_file = open('urls.txt','r')

for url in url_file.readlines():
   print(url)
   url_check = ('http://archive.org/wayback/available?url=' + url)
   r = requests.get(url_check)
   response_data = r.json()
   print(response_data)
   if response_data['archived_snapshots']:
      print(url + ' has already been captured at ' + response_data['archived_snapshots']['closest']['url'])
      file = open('existing_urls.txt', 'a')
      file.write(response_data['archived_snapshots']['closest']['url'])
      file.close()
   else:
      print('Capturing...')
      savepagenow.capture(url)
      archived_url = savepagenow.capture(url)
      print(archived_url)
      file = open('archived_urls.txt', 'a')
      file.write(archived_url)
      file.close()
   
url_file.close()
