import requests
import time
from bs4 import BeautifulSoup
personCode = input("Enter the code of the person you are looking for \n>>")
codeURL = "https://www.southampton.ac.uk/people/"+personCode
request = requests.get(codeURL)

soup = BeautifulSoup(request.text, "html.parser")
nameElement = soup.find_all("h1", {"class": f"heading-m inline-block text-prussianDark"})
if nameElement == []:
    print("No Usr Found")
else:   
    print(nameElement[0].text)