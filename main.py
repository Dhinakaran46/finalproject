import subprocess
import extract
import static

def run_extract():
    """Run the extract.py script to fetch and save HTML content."""
    try:
        subprocess.run(['python', 'extract.py'], check=True)
        print("Successfully executed extract.py")
    except subprocess.CalledProcessError as e:
        print(f'Error running extract.py: {e}')

def run_static():
    """Run the static.py script to upload the HTML content to S3."""
    try:
        subprocess.run(['python', 'static.py'], check=True)
        print("Successfully executed static.py")
    except subprocess.CalledProcessError as e:
        print(f'Error running static.py: {e}')

if __name__ == '__main__':
    run_extract()  # First, extract the HTML content
    run_static()   # Then, upload it to S3

# import requests

# # URL of the webpage you want to retrieve
# url = 'https://www.google.co.in/'

# try:
#     # Make the GET request
#     response = requests.get(url)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Save the HTML content to index.html
#         with open('index.html', 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         print('HTML content saved to index.html')
#     else:
#         print(f'Error {response.status_code}: {response.text}')

# except requests.exceptions.RequestException as e:
#     print(f'Request failed: {e}')
