# Extract oyoroom data (Hotel Name and Price) using Beautifulsoup library
from bs4 import BeautifulSoup
import requests

results = requests.get("https://www.oyorooms.com/hotels-in-madhapur-hyderabad/")

# To check whether the website is acessible or not we use status_code
# If the output is 200 it is ok.
print(results.status_code)

# Store the page content of the website accessed
response = results.content

# Create BeautifulSoup object from the BeautifulSoup class based on the source variable
soup = BeautifulSoup(response,'lxml')

def get_hotel_info(soup):
    hotel_info = soup.find_all("div",class_="oyo-cell--12-col oyo-cell--8-col-tablet oyo-cell--4-col-phone")
    if hotel_info:
        hotel_price = None
        hotel_name = None
        for tag in hotel_info: 
            name_temp = tag.find("h3",class_="listingHotelDescription__hotelName d-textEllipsis")
            if name_temp is not None:
                hotel_name = name_temp.text
            price_temp = tag.find("span",class_="listingPrice__finalPrice")
            if price_temp is not None:
                hotel_price = price_temp.text[1:]
            if hotel_name and hotel_price:
                print(hotel_name,':'hotel_price)

if soup:
    # hotel_info for the current page
    get_hotel_info(soup)

# Extract the links for the remaining pages
all_pages = soup.find_all("a",class_="link ListingPagination__pageContainer--page")
links = set()

for page in all_pages:
    links.add(page["href"])

# hotel_info for the remaining pages
if links:
    for next_page in links:
        url = 'https://www.oyorooms.com' + next_page
        page_results = requests.get(url)
        page_response = page_results.content
        soup = BeautifulSoup(page_response,'lxml')
        get_hotel_info(soup)

