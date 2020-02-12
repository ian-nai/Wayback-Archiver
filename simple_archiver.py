import savepagenow

url_file = open('urls.txt','r')

for url in url_file.readlines():
   print(url)
   savepagenow.capture(url)
   archived_url = savepagenow.capture(url)
   print(archived_url)
   file = open('archived_urls.txt', 'a')
   file.write(archived_url)
   file.close()
   
url_file.close()
