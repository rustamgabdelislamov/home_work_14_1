from src.utils import read_json

from unittest.mock import mock_open, patch


@patch('builtins.open', new_callable=mock_open, read_data='{"key": "value"}')
def test_read_json(mock_file):
    # Теперь вызов open() будет использовать mock_open
    result = read_json('dummy_path.json')

    # Проверяем, что функция вернула правильный словарь
    assert result == {"key": "value"}

    # Проверяем, что open() был вызван с правильными аргументами
    mock_file.assert_called_once_with('dummy_path.json', 'r', encoding='UTF-8')
