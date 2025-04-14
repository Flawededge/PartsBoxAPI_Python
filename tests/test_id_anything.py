import pytest
import os
from dotenv import load_dotenv
from src.PartsBoxAPI.PartsBoxAPI import PartsBoxAPI

load_dotenv()

@pytest.fixture
def partsbox_api():
    api_key = os.getenv("PARTSBOX_TEST_API_KEY")
    return PartsBoxAPI(api_key=api_key)

def test_id_anything_api_initialization(partsbox_api):
    assert partsbox_api.id_anything is not None