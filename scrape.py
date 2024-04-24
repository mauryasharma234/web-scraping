# Importing BeautifulSoup and 
# it is in the bs4 module 
from bs4 import BeautifulSoup 

# Opening the html file. If the file 
# is present in different location, 
# exact location need to be mentioned 
HTMLFileToBeOpened = open("global.html", "r") 

# Reading the file and storing in a variable 
contents = HTMLFileToBeOpened.read() 

# Creating a BeautifulSoup object and 
# specifying the parser 
beautifulSoupText = BeautifulSoup(contents, 'html.parser') 

results = beautifulSoupText.find(id="main")

operators = results.find_all("span", class_="signature")
# print(results.prettify())

print("Signature:", len(operators))
for operator in operators:
    print(operator.text)

# operators = results.find_all("div", class_="name")

# for operator in operators:
#     print(operator.text)


# Using the prettify method to modify the code 
# Prettify() function in BeautifulSoup helps 
# to view about the tag nature and their nesting 
# print(beautifulSoupText.body.prettify()) 


# for tag in beautifulSoupText.findAll(True): 
#     print(tag.name, " : ", len(beautifulSoupText.find(tag.name).text)) 