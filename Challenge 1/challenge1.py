import requests
from bs4 import BeautifulSoup
personCode = input("Enter the code of the person you are looking for \n>>")
codeURL = "https://www.ecs.soton.ac.uk/people/"+personCode

request = requests.get(codeURL)
soup = BeautifulSoup(request.text, "html.parser")
nameElement = soup.find_all("a", {"href": "/people/dem"})
print(nameElement[0].text)