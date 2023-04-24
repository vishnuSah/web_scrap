import requests
from bs4 import BeautifulSoup
import pandas as pd 

"""
Scraping Flipkart page, Extracting Name, Price and Images of Mobile Phone device and storing it in to CSV file 
using Pandad DataFrame

"""

try :
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme"
    response = requests.get(url)

    htmlcontent =  response.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')

    Titles = []
    Prices = []
    Images = []

    for d in soup.find_all('div', attrs= {'class':'_2kHMtA'}):
        title = d.find('div', attrs= {'class':'_4rR01T'})
        Titles.append(title.string)

        price = d.find('div', attrs= {'class':'_30jeq3 _1_WHN1'})
        Prices.append(price.string)

        image = d.find('img', attrs= {'class':'_396cs4'})
        Images.append(image.get('src'))


    Flipkart = pd.DataFrame({'Titles': Titles,
                            'Prices': Prices,
                            'Images':Images})

    Flipkart.to_csv("flipKartScrap.csv", index=False)
    
except Exception as e:
    print(e)