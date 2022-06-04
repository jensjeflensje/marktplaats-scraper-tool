import requests
import json


class ListingSeller:
    def __init__(self, name, is_verified):
        self.name = name
        self.is_verified = is_verified


class Listing:
    def __init__(self, title, description, seller, price, link, img, category_id, attributes):
        self.title = title
        self.description = description
        self.seller = seller
        self.price = price
        self.link = link
        self.img = img
        self.category_id = category_id
        self.attributes = attributes


class Marktplaats:

    def __init__(self, query, zip="", distance=1000000, pricefrom=0, priceto=1000000, limit=0, offset=0):
        self.request = requests.get(
            "https://www.marktplaats.nl/lrp/api/search",
            params={
                "attributeRanges[]":  [
                    f"PriceCents:{pricefrom * 100}:{priceto * 100}",
                ],
                "limit": str(limit),
                "offset": str(offset),
                "query": str(query),
                "searchInTitleAndDescription": "true",
                "viewOptions": "list-view",
                "distanceMeters": str(distance),
                "postcode": zip,
            },
            # Some headers to make the request look legit
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
                "Accept": "application/json",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
            }
        )

        self.body = self.request.text
        self.body_json = json.loads(self.body)

    def get_listings(self):
        listings = []
        for listing in self.body_json["listings"]:
            listing_obj = Listing(
                listing["title"],
                listing["description"],
                ListingSeller(listing["sellerInformation"]["sellerName"], listing["sellerInformation"]["isVerified"]),
                listing["priceInfo"]["priceCents"] / 100,
                "https://link.marktplaats.nl/" + listing["itemId"],
                listing["pictures"][0]["mediumUrl"],
                listing["categoryId"],
                listing["attributes"],
            )
            listings.append(listing_obj)
        return listings
