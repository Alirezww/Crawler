import requests
from data import save_data_file


# if we have website with pagination :
def start_crawl(url):
    crawl = True
    page = 0
    while crawl:
        page += 1
        response = requests.get(url.format(page))
        crawl = bool(response.url == url.format(page))
        if crawl and response.status_code == 200:
            save_data_file(response)
    print(f'{page - 1} pages found for given address.')


# if we dont have any pagination in website :
# def start_crawl(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         save_data_file(response)
#     else:
#         print('There is an error !!')


if __name__ == '__main__':
    target = 'https://emalls.ir/%D9%85%D8%AD%D8%B5%D9%88%D9%84%D8%A7%D8%AA~Category~39~b~Samsung~page~{}'
    start_crawl(target)
