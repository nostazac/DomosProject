
from geopy.geocoders import Nominatim

loc = Nominatim(user_agent = "Geopy Library")

getLoc = loc.geocode("Izmir")

print("Longitude = ", getLoc.latitude,"\n")
print("Longitude = ", getLoc.longitude)
