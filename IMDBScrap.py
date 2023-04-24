import requests
from bs4 import BeautifulSoup
import openpyxl

"""
Scraping Movie Name, Rank, Year of release and imdb rating from IMDB wesite.

"""

try :
    response = requests.get("https://www.imdb.com/chart/top/")
    soup = BeautifulSoup(response.text, "html.parser")

    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = 'IMDB Top Movies'

    sheet.append(['Rank', 'Movie', 'Year', 'IMDB Rating'])

    Movies = soup.find('tbody', class_='lister-list').find_all('tr')

    for movie in Movies:
        name = movie.find('td', class_= 'titleColumn').find('a').text

        rank = movie.find('td', class_= 'titleColumn').get_text(strip=True).split('.')[0]
        rank = int(rank)

        year = movie.find('td', class_= 'titleColumn').find('span', class_ = 'secondaryInfo').text.strip('()')
        year = int(year)

        rating = movie.find('td', class_= 'ratingColumn imdbRating').text
        rating = float(rating)

        sheet.append([rank, name, year, rating])

    excel.save('IMDB Top Movies Scrap.xlsx')

except Exception as e:
    print(e)