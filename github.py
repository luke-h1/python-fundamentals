import pip._vendor.requests as requests

def create_query(languages, min_stars=50000):
    query = f'stars:>{min_stars} '
    for language in languages: 
        query += f'language:{language} '

    return query

def repos_with_most_stars(languages):
    API_URL = 'https://api.github.com/search/repositories'
    query = create_query(languages)
    parameters = {'q': query, "sort": 'stars', 'order': 'desc'}
    response = requests.get(API_URL, params=parameters)
    response_json = response.json()['items']
    return response_json
    

if __name__ == '__main__':
    # main method goes here
    languages = ['python', 'javascript']
    results = repos_with_most_stars(languages)
    for result in results: 
        language = result['language']
        stars = result['stargazers_count']
        name = result['name']
        print(f'-> {name} is a {language} repo with {stars} stars')

