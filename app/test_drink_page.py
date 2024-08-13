import pytest
from unittest.mock import patch, MagicMock, mock_open
import streamlit as st
import drink_page
from drink_page import generate_recipe, generate_image, download_recipe, download_image

@pytest.fixture(autouse=True)
def setup_streamlit_env(monkeypatch):
    # Set default session state values or mock specific Streamlit functions.
    # Example: monkeypatch.setattr(st.session_state, 'page_name', "drink_page.py", raising=False)
    monkeypatch.setitem(st.session_state, 'page_name', "drink_page.py")
    # Additional mocking as necessary

@pytest.fixture(autouse=True)
def setup_tests(monkeypatch):
    # Mocking session_state requires using monkeypatch.setattr
    monkeypatch.setattr(drink_page.st, 'session_state', {'page_name': 'drink_page.py'}, raising=False)
    # Mock other st elements here as needed for your tests
    monkeypatch.setattr(drink_page.st, 'text_input', lambda _: "Orange", raising=False)
    monkeypatch.setattr(drink_page.st, 'selectbox', lambda _, __: "Cocktail", raising=False)
    monkeypatch.setattr(drink_page.st, 'button', lambda _: True, raising=False)
    monkeypatch.setattr(drink_page.st, 'write', MagicMock(), raising=False)
    monkeypatch.setattr(drink_page.st, 'image', MagicMock(), raising=False)
    monkeypatch.setattr(drink_page.st, 'markdown', MagicMock(), raising=False)

def test_ingredient_input():
    ingredients = {"Orange"}
    assert generate_recipe(ingredients, "Cocktail") != ""

def test_drink_type_selection():
    assert generate_recipe(set(), "Smoothie") != ""

def test_generate_recipe_button_no_ingredients():
    assert generate_recipe(set(), "Cocktail") != ""

@pytest.mark.parametrize("ingredients,drink_type,expected", [
    ({"Banana"}, "Mocktail", "Sample Recipe"),  # Expected outcomes adjusted to realistic use case
])
def test_generate_recipe_button_with_ingredients(ingredients, drink_type, expected):
    with patch("drink_page.genai.GenerativeModel.generate_content", return_value=MagicMock(text=expected)):
        assert generate_recipe(ingredients, drink_type) == expected

def test_generate_image():
    with patch("drink_page.generate_image", return_value="drink_image.jpg") as mock_generate:
        assert generate_image("drink_image.jpg") == "drink_image.jpg"

def test_download_recipe(monkeypatch):
    monkeypatch.setattr("builtins.open", mock_open(read_data="sample data"))
    download_recipe("Sample Recipe")


def test_download_image(monkeypatch):
    mock_file_read = mock_open(read_data=b"fake image data")
    monkeypatch.setattr("builtins.open", mock_file_read)


def test_drink_type_selection():
    drink_page.st.selectbox.return_value = "Smoothie"
    result = generate_recipe({"Milk", "Fruits"}, "Smoothie")
    assert result != ""

