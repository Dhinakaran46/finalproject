import requests

# URL of the webpage you want to retrieve
url = 'https://www.codeproject.com/'

try:
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the HTML content to index.html
        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        print('HTML content saved to index.html')
    else:
        print(f'Error {response.status_code}: {response.text}')

except requests.exceptions.RequestException as e:
    print(f'Request failed: {e}')