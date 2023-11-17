import pytest
from fastapi.testclient import TestClient

from main import app


class GetFormTestData:
    PHONE = "+7 8 812 234-56-77"
    EMAIL = "email@example.com"


class TestGetForm:
    path = app.url_path_for("get_form")

    def test_success(self, client: TestClient) -> None:
        response = client.post(
            self.path,
            params={
                "phone": GetFormTestData.PHONE,
                "email": GetFormTestData.EMAIL,
            }
        )
        parsed_response = response.json()
        assert "form_name" in parsed_response
        assert parsed_response["form_name"]

    def test_form_not_found(self, client: TestClient) -> None:
        response = client.post(
            self.path,
            params={
                "non_exists_field_1": GetFormTestData.PHONE,
                "non_exists_field_2": GetFormTestData.EMAIL,
            }
        )
        parsed_response = response.json()
        assert "non_exists_field_1" in parsed_response
        assert "non_exists_field_2" in parsed_response
        assert parsed_response["non_exists_field_1"] == "PHONE"
        assert parsed_response["non_exists_field_2"] == "EMAIL"


if __name__ == '__main__':
    pytest.main()
