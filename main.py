import scrap_akuma_no_mi
import json_manager

URL = 'https://onepiece.fandom.com/wiki'


if __name__ == '__main__':
    data = scrap_akuma_no_mi.get_all()
    json_manager.save_to_json(data, 'akuma_no_mi.json')
