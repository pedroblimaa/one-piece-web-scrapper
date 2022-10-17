import scrap.scrap_akuma_no_mi as scrap_akuma_no_mi
import scrap.scrap_characters as scrap_characters
import utils.json_manager as json_manager

URL = 'https://onepiece.fandom.com/wiki'


if __name__ == '__main__':
    data = scrap_characters.get_all()
    json_manager.save_to_json(data, 'characters.json')
