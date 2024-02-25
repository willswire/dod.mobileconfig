import requests
from bs4 import BeautifulSoup
import zipfile
import io
import plistlib

def download_zip_file(url):
    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    zip_file.extractall()
    print("Zip file extracted.")

def modify_mobileconfig(cert_file, mobileconfig_path):
    with open(cert_file, 'r') as file:
        lines = file.readlines()[1:-1]  # Remove the first and last line
        cert_data = ''.join(lines).replace('\n', '')

    with open(mobileconfig_path, 'rb') as file:
        plist = plistlib.load(file)

    plist['PayloadContent'][0]['PayloadContent'] = cert_data

    with open(mobileconfig_path, 'wb') as file:
        plistlib.dump(plist, file)

    print(f"Modified {mobileconfig_path} successfully.")

def main():
    page_url = "https://public.cyber.mil/announcement/new-dod-pki-cas-released/"
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    zip_link = ""

    for link in soup.find_all('a', href=True):
        if ".zip" in link['href'] and "cert" in link['href']:
            zip_link = link['href']
            break

    if zip_link:
        download_zip_file(zip_link)
        modify_mobileconfig('certificates_pkcs7_v5_13_dod/dod_pke_chain.pem', 'dod.mobileconfig')
    else:
        print("No zip file link found.")

if __name__ == "__main__":
    main()
