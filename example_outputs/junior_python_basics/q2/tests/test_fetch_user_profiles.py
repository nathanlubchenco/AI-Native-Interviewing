import sys
import pathlib

# Ensure q2 directory is on path for imports
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
import requests

from fetch_user_profiles import fetch_user_profile

class DummyResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"Status code: {self.status_code}")

def test_fetch_user_profile_success(monkeypatch):
    # Simulate valid response with email
    monkeypatch.setattr(requests, 'get', lambda url: DummyResponse({'email': 'test@example.com'}))
    email = fetch_user_profile(123)
    assert email == 'test@example.com'

def test_fetch_user_profile_missing_email(monkeypatch):
    # Simulate response missing 'email'
    monkeypatch.setattr(requests, 'get', lambda url: DummyResponse({'name': 'Test User'}))
    with pytest.raises(KeyError):
        fetch_user_profile(123)

def test_fetch_user_profile_http_error(monkeypatch):
    # Simulate non-200 status code
    monkeypatch.setattr(requests, 'get', lambda url: DummyResponse({'error': 'not found'}, status_code=404))
    with pytest.raises(requests.HTTPError):
        fetch_user_profile(123)