import wget
url = 'https://www.7-zip.org/a/7z2107-x64.exe'
filename = wget.download(url)
filename 
'7-zip_64.exe'

