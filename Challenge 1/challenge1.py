import requests
from bs4 import BeautifulSoup
import json
personCode = input("Enter the code of the person you are looking for \n>>")
codeURL = "https://www.southampton.ac.uk/people/"+personCode
request = requests.get(codeURL)

soup = BeautifulSoup(request.text, "html.parser")
nameElement = soup.find_all("script", {"type": f"application/ld+json"})
personDetails = json.loads(nameElement[0].get_text())['@graph']

print([dict(detail) for detail in personDetails if "Person" in detail.values()][0]['name'])
