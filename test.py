from marktplaats2 import Marktplaats

mp_object = Marktplaats("fiets", zip="1016LV", distance=10000, pricefrom=0, priceto=100, limit=1, offset=0)

listings = mp_object.get_listings()

for listing in listings:
    print(listing.title)
    print(listing.description)
    print(listing.seller.name)
    print(listing.price)
    print(listing.link)
    print(listing.img)
