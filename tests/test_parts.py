import pytest
from src.PartsBoxAPI.PartsBoxAPI import PartsBoxAPI
import os
from dotenv import load_dotenv

load_dotenv()

# This test needs at least 1 part to exist in the database

@pytest.fixture
def partsbox_api():
    api_key = os.getenv("PARTSBOX_TEST_API_KEY")
    return PartsBoxAPI(api_key=api_key)

def test_parts_api_initialization(partsbox_api):
    assert partsbox_api.parts is not None