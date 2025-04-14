# pylint: disable=missing-function-docstring, redefined-outer-name
import os
from dotenv import load_dotenv
import pytest
from PartsBoxAPI import PartsBoxAPI

load_dotenv()

LOCAL_PART_NAME = "RNF14FTD1M82"  # Hopefully a 1.82MΩ through hole resistor won't affect you

@pytest.fixture
def partsbox_api():
    api_key = os.getenv("PARTSBOX_TEST_API_KEY")
    return PartsBoxAPI(api_key=api_key)

def test_parts_api_initialization(partsbox_api:PartsBoxAPI):
    assert partsbox_api.parts is not None
    
def test_get_all_parts(partsbox_api: PartsBoxAPI):
    response = partsbox_api.parts.get_all_parts()
    assert response["partsbox.status/category"] == "ok"
    assert response['partsbox.status/message'] == "OK"
    assert isinstance(response["data"], list)  # Ensure the response contains a list of parts

def test_create_local_part(partsbox_api: PartsBoxAPI):
    created_parts = []
    try:
        response = partsbox_api.parts.create_part(
            part_type="local",
            part_name="TEST_LOCAL",
            part_description="test_description_TEST_LOCAL",
            part_notes="test_notes_TEST_LOCAL",
            part_tags=["test_tag_1", "test_tag_2"],
            part_footprint="test_footprint_TEST_LOCAL",
            part_attrition={"percentage": 5, "quantity": 1},
            part_low_stock={"report": 10}
        )
        assert response["partsbox.status/category"] == "ok"
        assert response["partsbox.status/message"] == "Part created"
        created_parts.append(response["data"]["part/id"])

        part_details = partsbox_api.parts.get_part(response["data"]["part/id"])
        assert part_details["partsbox.status/category"] == "ok"
        assert part_details["partsbox.status/message"] == "OK"
        assert part_details["data"]["part/name"] == "TEST_LOCAL"
    finally:
        for part_id in created_parts:
            delete_response = partsbox_api.parts.delete_part(part_id)
            assert delete_response["partsbox.status/category"] == "ok"
            assert delete_response['partsbox.status/message'] == "Part (or parts) deleted"

def test_create_meta_part(partsbox_api: PartsBoxAPI):
    created_parts = []
    try:
        response = partsbox_api.parts.create_part(
            part_type="meta",
            part_name="TEST_META",
            part_description="test_description_TEST_META",
            part_notes="test_notes_TEST_META",
            part_tags=["test_tag_1", "test_tag_2"],
            part_footprint="test_footprint_TEST_META",
            part_attrition={"percentage": 5, "quantity": 1},
            part_low_stock={"report": 10}
        )
        assert response["partsbox.status/category"] == "ok"
        assert response["partsbox.status/message"] == "Part created"
        created_parts.append(response["data"]["part/id"])

        part_details = partsbox_api.parts.get_part(response["data"]["part/id"])
        assert part_details["partsbox.status/category"] == "ok"
        assert part_details["partsbox.status/message"] == "OK"
        assert part_details["data"]["part/name"] == "TEST_META"
    finally:
        for part_id in created_parts:
            delete_response = partsbox_api.parts.delete_part(part_id)
            assert delete_response["partsbox.status/category"] == "ok"
            assert delete_response['partsbox.status/message'] == "Part (or parts) deleted"