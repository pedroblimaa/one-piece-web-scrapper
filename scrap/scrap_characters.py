import utils.utils as utils

URL = 'https://onepiece.fandom.com/wiki'
CHARS_URL = URL + '/List_of_Canon_Characters'

def get_all():
    get_chars()


def get_chars():
    html = utils.get_html(CHARS_URL)

    tables = html.findAll('table', class_='wikitable')
    table = tables[0]

    rows = table.find_all('tr')
    charNames = []

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        if len(cols) > 1:
            charNames.append(cols[1])

    charsInfo = get_chars_info(charNames)
    print(charsInfo)


def get_chars_info(charNames):
    charsUrls = []

    for charName in charNames:
        charUrl = URL + '/' + charName
        charsUrls.append(charUrl)

    evaluate_chars_info(charsUrls)

def evaluate_chars_info(charsUrls):
    print('Before get_multiple_html')
    charsHtml = utils.get_multiple_html(charsUrls)
    print('After get_multiple_html')
    charsInfo = []

    for charUrl, charHtml in zip(charsUrls, charsHtml):
        charInfo = evaluate_char_html(charHtml)
        if(charInfo is not None):
            charInfo['name'] = get_char_name_by_url(charUrl) 
            charsInfo.append(charInfo)

    return charsInfo

def evaluate_char_html(html):
    imgTag = html.find('img', class_='pi-image-thumbnail')
    img = imgTag['src'] if imgTag is not None else None
    description = get_char_description(html)

    if(img is not None and description is not None):
        return {
            'img': img,
            'description': description
        }
    else:
        return None

def get_char_description(html):
    descriptionTag =  html.find('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    description = descriptionTag.find('div', class_='pi-data-value pi-font')
    return  description.text if description is not None else None

def get_char_name_by_url(url):
    return url.split('/')[-1].replace('_', ' ')
