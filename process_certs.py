import requests
from bs4 import BeautifulSoup
import zipfile
import io
import plistlib
import base64

def download_and_extract_zip(url):
    """
    Downloads a ZIP file from the given URL and extracts its contents.

    :param url: URL of the ZIP file to download.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall()
        print("Zip file downloaded and extracted.")
    except requests.RequestException as e:
        print(f"Error downloading ZIP file: {e}")
    except zipfile.BadZipFile as e:
        print(f"Error extracting ZIP file: {e}")

def modify_mobileconfig(cert_file, mobileconfig_path):
    """
    Modifies the .mobileconfig file to include a new certificate, omitting the 
    BEGIN and END certificate lines and encoding the certificate data as binary.

    :param cert_file: Path to the PEM file containing the new certificate.
    :param mobileconfig_path: Path to the .mobileconfig file to be modified.
    """
    try:
        with open(cert_file, 'r') as file:
            lines = file.readlines()[1:-1]  # Remove the BEGIN and END certificate lines
            cert_data = ''.join(lines).replace('\n', '')

        cert_data_bytes = base64.b64decode(cert_data)

        with open(mobileconfig_path, 'rb') as file:
            plist = plistlib.load(file)

        plist['PayloadContent'][0]['PayloadContent'] = cert_data_bytes

        with open(mobileconfig_path, 'wb') as file:
            plistlib.dump(plist, file)

        print(f"Successfully modified {mobileconfig_path}.")
    except Exception as e:
        print(f"Error modifying .mobileconfig file: {e}")

def main():
    """
    Main function to automate the process of updating the .mobileconfig file
    with the latest DoD certificates.
    """
    page_url = "https://public.cyber.mil/announcement/new-dod-pki-cas-released/"
    try:
        response = requests.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        zip_link = ""

        for link in soup.find_all('a', href=True):
            if ".zip" in link['href'] and "cert" in link['href']:
                zip_link = link['href']
                break

        if zip_link:
            download_and_extract_zip(zip_link)
            modify_mobileconfig('certificates_pkcs7_v5_13_dod/dod_pke_chain.pem', 'dod.mobileconfig')
        else:
            print("No suitable ZIP file link found.")
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")

if __name__ == "__main__":
    main()
