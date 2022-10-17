import utils.utils as utils
import re

URL = 'https://onepiece.fandom.com/wiki'
TYPES = ['Paramecia', 'Zoan', 'Logia']
URL_CATEGORY = URL + '/Category:'


def get_all():
    akumaNoMiList = []

    for type in TYPES:
        akumaNoMiList.extend(get_akuma_no_mi(type))

    return akumaNoMiList


def get_akuma_no_mi(type):

    html = utils.get_html(URL_CATEGORY + type)

    div = html.find('div', class_='category-page__members')
    members = div.find_all('li', class_='category-page__member')

    akumaNoMiList = []

    for member in members:
        akumaNoMi = evaluate_akuma_no_mi_member(member, type)

        if akumaNoMi is not None:
            akumaNoMiList.append(akumaNoMi)

    akumaNoMiList = evaluate_akuma_no_mi_descriptions(akumaNoMiList)

    return akumaNoMiList


def evaluate_akuma_no_mi_member(member, type):
    link = member.find('a', class_='category-page__member-link')
    img = member.find('img', class_='category-page__member-thumbnail')

    if (link and img) is not None:
        evaluatedAkumaNoMi = evaluate_akuma_no_mi(link, img, type)
        return evaluatedAkumaNoMi

    return None


def evaluate_akuma_no_mi_descriptions(akumaNoMiList):
    akumaNoMiUrlList = []

    for akumaNoMi in akumaNoMiList:
        akumaNoMiLabelList = akumaNoMi['name'].split(' ')
        akumaNoMiLabel = '_'.join(akumaNoMiLabelList)
        akumaNoMiUrl = URL + '/' + akumaNoMiLabel
        akumaNoMiUrlList.append(akumaNoMiUrl)

    akumaNoMiHtmlList = utils.get_multiple_html(akumaNoMiUrlList)

    for akumaNoMi, akumaNoMiHtml in zip(akumaNoMiList, akumaNoMiHtmlList):
        print(akumaNoMi['name'])
        akumaNoMi['description'] = get_akuma_no_mi_description(akumaNoMiHtml)
        akumaNoMiList.append(akumaNoMi)

    return akumaNoMiList


def get_akuma_no_mi_description(html):
    div = html.find('div', class_='mw-parser-output')
    possibleDescriptions = div.findAll('p')
    for possibleDescription in possibleDescriptions:
        if possibleDescription.text[:10].find('The') != -1:
            return possibleDescription.text

    return None


def evaluate_akuma_no_mi(link, img, type):
    img['src'] = replace_img_size(img['src'], '400', '300')

    return {
        'name': link.text,
        'image': img['src'],
        'type': type
    }


def replace_img_size(img, newWidth, newHeight):
    imgWidthRegex = re.compile(r'width/(\d+)')
    imgHeightRegex = re.compile(r'height/(\d+)')
    img = imgWidthRegex.sub('width/' + newWidth, img)
    img = imgHeightRegex.sub('height/' + newHeight, img)

    return img
