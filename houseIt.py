#! python3

# houseIt.py - Launches idealista.com in the browser using the adresses
# in the files inside the input_directory
# If the input_directory doesn't exist or no input_directory is specified
# idealista.com is launched

import webbrowser, sys, os
import requests, bs4
import urllib

##### Constants #####
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0',
}

WEBSITE = 'https://www.idealista.com'


##### Generic Functions #####
def get_addresses_from_file(file_path):
    with open(file_path) as txt_file:
        return [line.strip() for line in txt_file]

def get_addresses(file_list):
    try:
        address_list = []
        for file_path in file_list:
            address_list += get_addresses_from_file(file_path)
        return address_list
    except:
        return ['']

address_list = []


##### Input #####
if len(sys.argv) > 1:
    input_dir = sys.argv[1]
else:
    input_dir = None


#if len(sys.argv) > 1:
#    input_dir = sys.argv[1]
#    try:
#        file_list = [os.path.join(input_dir, fil) for fil in os.listdir(input_dir)]
#        address_list += get_addresses(file_list)
#    except:
#        address_list += ['']
#else:
#    address_list += ['']
#
#downloaded_pages = []
#for address in address_list:
#    res = requests.get(website + address, headers=HEADERS)
#    res.raise_for_status()
#    soup = bs4.BeautifulSoup(res.text, 'html.parser')
#    articles = soup.select('article')
#        
#    houses = []
#    for article in articles:
#        dictio = {}
#        try:
#            a_tag = article.select('.item-link')[0]
#        except:
#            continue
#        dictio['url'] = a_tag.attrs['href']
#        dictio['title'] = a_tag.text
#        houses += [dictio]


##### Website #####
class Website:
    headers = HEADERS

    def __init__(self, website, input_directory):
        self.website = website 
        self.input_directory = input_directory 
        self.input_files = self.get_file_list()

    def get_file_list(self):
        try:
            return [os.path.join(self.input_directory, f) for f in os.listdir(self.input_directory)]
        except:
            return f'Could not get files in {self.input_directory}'

    def get_addresses(self):
        try:
            address_list = []
            for file_path in self.input_files:
                address_list += get_addresses_from_file(file_path)
            return address_list
        except:
            return f'Could not get any addresses'

    def request(self):
        website = urllib.parse.urljoin(self.website, address)
        res = requests.get(website, headers=self.headers)
        res.raise_for_status()


idealista = Website(WEBSITE, input_dir)
import ipdb; ipdb.set_trace()
