import pytest
from src.PartsBoxAPI.PartsBoxAPI import PartsBoxAPI
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def partsbox_api():
    api_key = os.getenv("PARTSBOX_TEST_API_KEY")
    return PartsBoxAPI(api_key=api_key)

def test_orders_api_initialization(partsbox_api):
    assert partsbox_api.orders is not None