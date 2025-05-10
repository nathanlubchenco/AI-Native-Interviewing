"""
fetch_user_profiles.py: Fetch user profile email from external API.
"""
import requests

def fetch_user_profile(user_id: int) -> str:
    """
    Fetch a user profile by ID and return the email address.
    Raises KeyError if 'email' is missing.
    Raises HTTPError for non-200 responses.
    """
    url = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # May raise KeyError if 'email' not in data
    return data['email']

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fetch user email from API.")
    parser.add_argument('user_id', type=int, help='User ID to fetch')
    args = parser.parse_args()
    email = fetch_user_profile(args.user_id)
    print(f"User email: {email}")

if __name__ == '__main__':
    main()