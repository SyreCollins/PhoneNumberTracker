from django.shortcuts import render
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium


def home(response):
    country = None
    carrier_name = None
    lat = None
    long = None
    map_html = ""

    if response.method == "POST":
        number = response.POST.get("phonenumber")
        theNumber = phonenumbers.parse(number)

        # Get the carrier name
        carrier_name = carrier.name_for_number(theNumber, "en")

        # Get the location description
        country = geocoder.description_for_number(theNumber, "en")
        API_KEY = ""

        # Use OpenCage to get the coordinates
        geolocator = OpenCageGeocode(API_KEY)
        location = geolocator.geocode(country)

        if location:
            # Get the latitude and longitude
            lat = location[0]["geometry"]["lat"]
            long = location[0]["geometry"]["lng"]

            # Create a map and add a marker
            myMap = folium.Map(location=[lat, long], zoom_start=9)
            folium.Marker([lat, long], popup=country).add_to(myMap)

            # Save the map
            # myMap.save("myLoc.html")

            # Render the map to HTML
            map_html = myMap._repr_html_()

    return render(
        response,
        "index.html",
        {
            "country": country,
            "carrier": carrier_name,
            "lat": lat,
            "long": long,
            "map_html": map_html,
        },
    )
