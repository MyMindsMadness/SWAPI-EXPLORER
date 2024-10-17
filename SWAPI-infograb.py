import requests
import json
import inquirer

def api_select():
    api_urls = ["people","planets","films","species","vehicles","starships", "quit"]
    questions = [
        inquirer.List(
            'option',
            message="Which API?",
            choices=api_urls,
            carousel=True
        )
    ]
    answer = inquirer.prompt(questions)
    return answer["option"]
    # for api_url in api_urls:
    #     return api_url

def json_getter(api):
    api_data=[]
    url = f"https://swapi.dev/api/{api}/"
    while url:
        result = requests.get(url=url).json()
        api_data.extend(result['results'])
        url = result['next']
    return api_data

def json_write_out(data, api):
    filename = f'localdata/{api}data.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    while True:
        api = api_select()
        if api == "quit":
            print ("Exiting program! Goodbye")
            break
        else:
            data = json_getter(api)
            json_write_out(data, api)

if __name__ == '__main__':
    main()
