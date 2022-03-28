from urllib.parse import urlparse

from parser import html_parse


def get_file_name(url):
    parsed = urlparse(url)
    parsed_list = parsed.path.split('/')
    filename = ''.join(parsed_list[1] + parsed.query.replace('=', '_'))
    filename += '.html'
    return filename


def save_data_file(response_obj):
    # with open(get_file_name(response_obj.url), 'w') as f:
    #     f.writelines(response_obj.text)
    return html_parse(response_obj.text)
