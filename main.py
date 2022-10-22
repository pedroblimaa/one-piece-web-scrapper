import scrap.scrap_akuma_no_mi as akuma_no_mi
import scrap.scrap_characters as characters
import utils.json_manager as json_manager

URL = 'https://onepiece.fandom.com/wiki'


def scrap_characters():
    data = characters.get_all()
    json_manager.save_to_json(data, 'characters.json')


def scrap_akuma_no_mi():
    data = akuma_no_mi.get_all()
    json_manager.save_to_json(data, 'akuma_no_mi.json')


if __name__ == '__main__':
    scrap_characters()
