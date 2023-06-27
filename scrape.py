import requests
from bs4 import BeautifulSoup

def scrape_property_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    properties = []

    # Find the container elements that hold the property details
    property_containers = soup.find_all('div', class_='m-srp-card__container')

    for container in property_containers:
        # Extract the details of each property
        title = container.find('a', class_='m-srp-card__title').text.strip()
        location = container.find('div', class_='m-srp-card__address').text.strip()
        price = container.find('div', class_='m-srp-card__price').text.strip()
        area_type = container.find('div', class_='m-srp-card__summary__title').text.strip()
        size = container.find('div', class_='m-srp-card__summary__info').text.strip()

        property_data = {
            'title': title,
            'location': location,
            'price': price,
            'area_type': area_type,
            'size': size
        }

        properties.append(property_data)

    return properties

# URL of the website you want to scrape
url = 'https://www.magicbricks.com/flats-for-rent-in-bangalore-pppfr'

# Call the function to scrape the data
property_data = scrape_property_data(url)

# Print the scraped property data
for property in property_data:
    print(f"Title: {property['title']}")
    print(f"Location: {property['location']}")
    print(f"Price: {property['price']}")
    print(f"Area Type: {property['area_type']}")
    print(f"Size: {property['size']}")
    print('hi')
    print()
