import pip._vendor.requests as requests


def repos_with_most_stars():
    API_URL = 'https://api.github.com/search/repositories'
    parameters = {'q': 'stars:>50000'}
    response = requests.get(API_URL, params=parameters)
    response_json = response.json()['items']
    return response_json
    

if __name__ == '__main__':
    # main method goes here
    results = repos_with_most_stars()
    for result in results: 
        language = result['language']
        stars = result['stargazers_count']
        name = result['name']
        print(f'-> {name} is a {language} repo with {stars} stars')
