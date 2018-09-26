from marktplaats import Marktplaats

#initialize the object with the query and all its available filters
mp_object = Marktplaats("i5-4460", zip="1016LV", distance=10000, pricefrom=0, priceto=100)

#get 5 listings, default limit is 10
listings = mp_object.get_listings(limit=5)


#loop all the 5 listings and print all their attributes
for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.link)
    print(listing.img)