import requests
import json
import inquirer
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def data_select():
    api_urls = ["people","planets","films","species","vehicles","starships", "quit"]
    questions = [
        inquirer.List(
            'option',
            message="Desired information: ",
            choices=api_urls,
            carousel=True
        )
    ]
    answer = inquirer.prompt(questions)
    return answer["option"]

def openfile(selection):
    filename = f'localdata/{selection}data.json'
    with open (filename) as f:
        data = json.load(f)
        return data

def name_get(data):
    search_list = []
    for i in data:
        search_list.append(i.get('name') or i.get('title'))
    return search_list

def Search(search_list, data):
    completer = WordCompleter(search_list, ignore_case=True)
    user_input = prompt("What information do you want to see? ", completer=completer)

    for i in data:
        if i.get("name") == user_input or i.get('title') == user_input:
            key = 'name'if 'name' in i else 'title'
            return i

def data_extractor(element_data, selected):
    if selected == 'people':
        parsed = people_builder(element_data)
        return parsed
    elif selected == 'planets':        
        parsed = planet_builder(element_data)
        return parsed
    elif selected == 'films':        
        parsed = film_builder(element_data)
        return parsed
    elif selected == 'species':
        parsed = species_builder(element_data)
        return parsed
    elif selected == 'vehicles': 
        parsed = vehicle_builder(element_data)
        return parsed       
    elif selected == 'starships':        
        parsed = spacecraft_builder(element_data)       
        return parsed

def people_builder(element_data):
    sections = [
    f'# {element_data["name"]}\n',
    f'## Personal Info\n',
    get_info("height", "HEIGHT",element_data),
    get_info("mass", "MASS",element_data),
    get_info("hair_color", "HAIR COLOUR",element_data),
    get_info("eye_color", "EYE COLOUR",element_data),
    get_info("skin_color", "SKIN COLOUR",element_data),
    get_info("gender", "GENDER",element_data),
    get_info("birth_year", "BIRTH YEAR",element_data),
    get_info("homeworld", "HOMEWORLD", element_data),
    f'## Vehicles & Starships\n',
    get_info("vehicles", "VEHICLES", element_data),
    get_info("starships", "STARSHIPS", element_data),
    f'## Appears in\n',
    get_info("films", "FILMS", element_data)
    ]
    return sections

def planet_builder(element_data):
    sections = [
    f'# {element_data["name"]}\n',
    f'## Planet Info\n',
    get_info("name", "NAME",element_data),
    get_info("rotation_period", "ROTATION PERIOD",element_data),
    get_info("orbital_period", "ORBITAL PERIOD",element_data),
    get_info("diameter", "DIAMETER",element_data),
    get_info("climate", "CLIMATE",element_data),
    get_info("gravity", "GRAVITY",element_data),
    get_info("terrain", "TERRAIN",element_data),
    get_info("surface_water", "SURFACE WATER",element_data),
    get_info("population", "POPULATION",element_data),
    f'## Notable Residents\n',
    get_info("residents", "RESIDENTS",element_data),
    f'## Appears in\n',
    get_info("films", "FILMS",element_data)
    ]
    return sections

def film_builder(element_data):
    sections = [
    f'# {element_data["title"]}\n',
    f'## Film Info\n',
    get_info("title", "TITLE",element_data),
    get_info("episode_id", "EPISODE",element_data),
    #get_info("opening_crawl", "OPENING CRAWL",element_data),
    get_info("director", "DIRECTOR",element_data),
    get_info("producer", "PRODUCER",element_data),
    get_info("release_date", "RELEASED",element_data),
    f'## Notable Characters & Species\n',
    get_info("characters", "CHARACTERS",element_data),
    get_info("species", "SPECIES",element_data),
    f'## Locations\n',
    get_info("planets", "PLANETS",element_data),
    f'## Vehicles & Starships\n',
    get_info("vehicles", "VEHICLES", element_data),
    get_info("starships", "STARSHIPS", element_data)
    ]
    return sections

def species_builder(element_data):
    sections = [
    f'# {element_data["name"]}\n',
    f'## Species Info\n',
    get_info("name", "NAME",element_data),
    get_info("classification", "CLASSIFICATION",element_data),
    get_info("designation", "DESIGNATION",element_data),
    get_info("homeworld", "HOMEWORLD",element_data),
    f'## Species Traits\n',
    get_info("average_height", "AVERAGE HEIGHT",element_data),
    get_info("average_lifespan", "AVERAGE LIFESPAN",element_data),
    get_info("skin_colors", "SKIN COLOURS",element_data),
    get_info("hair_colors", "HAIR COLOURS",element_data),
    get_info("eye_colors", "EYE COLOURS",element_data),
    f'## Notable Characters & Species\n',
    get_info("people", "CHARACTERS",element_data),
    f'## Appears in\n',
    get_info("films", "FILMS",element_data)
    ]
    return sections

def vehicle_builder(element_data):
    sections = [
    f'# {element_data["name"]}\n',
    f'## Vehicle Info\n',
    get_info("name", "NAME",element_data),
    get_info("model", "MODEL",element_data),
    get_info("manufacturer", "MANUFACTURE",element_data),
    get_info("cost_in_credits", "COST IN CREDITS",element_data),
    get_info("length", "LENGTH",element_data),
    get_info("max_atmosphering_speed", "SPEED",element_data),
    get_info("crew", "MAX CREW",element_data),
    get_info("passengers", "MAX PASSENGERS",element_data),
    get_info("cargo_capacity", "CARGO CAPACITY",element_data),
    get_info("consumables", "CONSUMABLES",element_data),
    get_info("vehicle_class", "CLASS",element_data),
    f'## Known Pilots Info\n',
    get_info("pilots", "PILOTS",element_data),
    f'## Appears in\n',
    get_info("films", "FILMS",element_data)
    ]
    return sections

def spacecraft_builder(element_data):
    sections = [
    f'# {element_data["name"]}\n',
    f'## Spacecraft Info\n',
    get_info("name", "NAME",element_data),
    get_info("model", "MODEL",element_data),
    get_info("manufacturer", "MANUFACTURE",element_data),
    get_info("cost_in_credits", "COST IN CREDITS",element_data),
    get_info("length", "LENGTH",element_data),
    get_info("max_atmosphering_speed", "SPEED",element_data),
    get_info("crew", "MAX CREW",element_data),
    get_info("passengers", "MAX PASSENGERS",element_data),
    get_info("cargo_capacity", "CARGO CAPACITY",element_data),
    get_info("consumables", "CONSUMABLES",element_data),
    get_info("hyperdrive_rating", "HYPERDRIVE",element_data),
    get_info("MGLT", "MGLT",element_data),
    get_info("starship_class", "CLASS",element_data),
    f'## Known Pilots Info\n',
    get_info("pilots", "PILOTS",element_data),
    f'## Appears in\n',
    get_info("films", "FILMS",element_data)
    ]
    return sections

def get_info(key, label, element_data):
    value = element_data[key]
    if isinstance(value, list):
        if not value:
            return ""  # Return empty string if the list is empty
        # Process each item in the list
        processed_items = []
        for item in value:
            if "https://" in str(item):
                processed_items.append(fetch_data_from_url(item))
            else:
                processed_items.append(item)
        return f'### {label.upper()}\n' + ''.join([f'#### {item}\n' for item in processed_items])

    if isinstance(value, str) and "https://" in value:
        fetched_name = fetch_data_from_url(value)
        return f'### {label.upper()}\n#### {fetched_name}\n'

    return f'### {label.upper()}\n#### {value}\n' if value is not None else ""

def fetch_data_from_url(url):
    response = requests.get(url)
    data = response.json()
    return data.get('name') or data.get('title') or 'Unknown'

def markmap_maker(element_data,extracted_data):
    md_content = ''.join(filter(None, extracted_data))
    fileparse = element_data.get('name') or element_data.get('title')
    filename = f'output/{fileparse}.md'
    with open(filename, "w") as file:
        file.write(md_content)

def main():
    while True:
        selected = data_select()
        if selected == "quit":
            print("Exiting the program. Goodbye!")
            break
        else:
            data = openfile(selected)
            search_list = name_get(data)
            element_data = Search(search_list,data)
            parsed = data_extractor(element_data, selected)
            markmap_maker(element_data, parsed)
    

if __name__ == '__main__':
    main()


