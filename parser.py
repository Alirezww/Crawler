from bs4 import BeautifulSoup


def extract_price(adv):
    cost = adv.find('span', 'item-price')
    return cost


def extract_data(adv):
    return dict(price=extract_price(adv))


def html_parse(data):
    soup = BeautifulSoup(data, 'html.parser')
    adv_div = soup.find(id='listdiv')  # find an element with its id
    # adv_div = soup.find("div", {"class": "cards"})  # find an element with the class or => soup.find("div","cards")
    adv_list = adv_div.find_all('div', {'class': 'item'})  # find elements with the class to list
    data = list()
    for adv in adv_list:
        data.append(extract_data(adv))
    return data
