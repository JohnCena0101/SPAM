import requests
import sys

def share_post(post_id, cookie):
    url = f'https://www.facebook.com/{post_id}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': cookie
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Extract necessary tokens or data from the response
            # This step depends on how Facebook's form submission works
            # You may need to parse the response content to find hidden fields, tokens, etc.

            # Simulate the share action
            share_url = 'https://www.facebook.com/ajax/sharer/?dpr=1'
            share_data = {
                'post_id': post_id,
                'privacyx': '300645083384735', # Public
                'share_type': 'on_timeline',
                # Add any other necessary data here
            }

            share_response = requests.post(share_url, headers=headers, data=share_data)
            if share_response.status_code == 200:
                print(f'Successfully shared the post: {post_id}')
            else:
                print(f'Failed to share the post: {post_id}')
        else:
            print(f'Failed to retrieve the post: {post_id}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python share.py <post_id> <cookie>')
        sys.exit(1)

    post_id = sys.argv[1]
    cookie = sys.argv[2]

    share_post(post_id, cookie)
