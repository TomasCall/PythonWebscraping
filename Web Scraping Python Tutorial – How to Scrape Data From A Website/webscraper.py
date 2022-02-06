from distutils.log import info
import requests
import csv
from bs4 import BeautifulSoup

########################################################
def first_excersize():
    my_request = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    txt = my_request.text
    status = my_request.status_code
    print("Text:")
    #print(f"{txt}")
    print(f"Status code: {status}")


def second_excersize():
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')
    page_title = soup.title.text
    print(f"Title:{page_title}")


def third_excersize():
    # Make a request
    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract title of page
    page_title = soup.title

    # Extract body of page
    page_body = soup.body

    # Extract head of page
    page_head = soup.head

    # print the result
    print(page_title, page_head)


def fourth_excersize():
    all_h1_tags = []
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract first <h1>(...)</h1> text
    tmp = soup.select('h1')
    for item in tmp:
        all_h1_tags.append(item.text)
    seventh_p_text = soup.select('p')[6].text
    print(f"All h1 tags: {all_h1_tags}")
    print(f"Seventh p tag:{seventh_p_text}")


def fifth_excersize():
    titles = []
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')
    tmp_titles = soup.select(".title")
    for item in tmp_titles:
        titles.append(item.text)

    ratings = []
    tmp_ps = soup.select(".ratings > p")
    for item in tmp_ps:
        ratings.append(item.text)

    top_items = []
    for i in range(len(titles)):
        title_and_ratings = {
            "title":titles[0].strip(),
            "ratings":ratings[0].strip()
        }
        top_items.append(title_and_ratings)
    print(top_items)
        
    #print()


def sixth_excersize():
    page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.select('a')
    links_with_data = []
    for a in links:
        data = {
            "href":a.get('href').strip(),
            "text":a.text.strip()
        }
        links_with_data.append(data)
    return links_with_data


def seventh_excersize():
    # Make a request
    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Create top_items as empty list
    all_products = []
    
    # Extract and store in top_items according to instructions on the left
    products = soup.select('div.thumbnail')
    for product in products:
        name = product.select('h4 > a')[0].text.strip()
        description = product.select('p.description')[0].text.strip()
        price = product.select('h4.price')[0].text.strip()
        reviews = product.select('div.ratings')[0].text.strip()
        image = product.select('img')[0].get('src')
    
        all_products.append({
            "name": name,
            "description": description,
            "price": price,
            "reviews": reviews,
            "image": image
        })
    
    
    keys = all_products[0].keys()
    
    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)


########################################################

########################################################
def first_example():
    res = requests.get('https://codedamn.com')
    print(res.text)
    print(res.status_code)


def second_example():
    page = requests.get("https://codedamn.com")
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.title.text
    print(f"Title:{title}")


def third_example():
    # Make a request
    page = requests.get("https://codedamn.com")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract title of page
    page_title = soup.title.text

    # Extract body of page
    page_body = soup.body

    # Extract head of page
    page_head = soup.head

    #print the result
    #print(page_body, page_head)
    print(page_head)


def fourth_example():
    page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract first <h1>(...)</h1> text
    first_h1 = soup.select('h1')[0].text
    print(first_h1)


def sixth_example():
    # Make a request
    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Create top_items as empty list
    image_data = []

    # Extract and store in top_items according to instructions on the left
    images = soup.select('img')
    for image in images:
        src = image.get('src')
        alt = image.get('alt')
        image_data.append({"src": src, "alt": alt})

    print(image_data)


def seventh_example():
    # Make a request
    page = requests.get(
        "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
    soup = BeautifulSoup(page.content, 'html.parser')

    all_products = []

    products = soup.select('div.thumbnail')
    for product in products:
        # TODO: Work
        print("Work on product here")


    keys = all_products[0].keys()

    with open('products.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_products)


########################################################
def main():
    #first_example()
    #first_excersize()
    #second_example()
    #second_excersize()
    #third_example()
    #third_excersize()
    #fourth_example()
    #fourth_excersize()
    #fifth_excersize()
    print(sixth_excersize())


if __name__=="__main__":
    main()