#import requests for requesting the to be scraped page and beautifulsoup for inspecting and filtering that scraped page
import requests
from bs4 import BeautifulSoup


#listing class that gets thrown in the list of listings
class Listing:

    #this now only has title, price, link and img but I am gonna add more soon!
    def __init__(self, title, price, link, img):
        self.title = title
        self.price = price
        self.link = link
        self.img = img


#marktplaats class for searching the query with its filters and returning it
class Marktplaats:

    def __init__(self, query, zip="1016LV", distance=1000000, pricefrom=0, priceto=1000000):
        self.request = requests.get("https://www.marktplaats.nl/z.html?query={query}&postcode={zip}&distance={distance}&priceTo={priceto}&priceFrom={pricefrom}".format(query=str(query), zip=str(zip), distance=str(distance), pricefrom=str(pricefrom), priceto=str(priceto)))
        self.body = self.request.text
        self.soup = BeautifulSoup(self.body, "html.parser")

    #sum up the listings and returning them
    def get_listings(self, limit=10):
        listings = []
        t = 0
        #take all articles and add them to the list
        for listing in self.soup.find_all("article"):
            if limit > t:
                listing_obj = Listing(
                    listing.find("span", attrs={'class':'mp-listing-title'}).text.strip()
                    , listing.find("span", attrs={'class': 'price-new'}).text.strip().replace("€ ", "")
                    , listing.find("a", attrs={'class': 'listing-table-mobile-link'})["href"].strip()
                    , "https:" + listing.find("img")["src"].strip()
                )
                listings.append(listing_obj)
                t += 1
            else:
                break
        return listings
