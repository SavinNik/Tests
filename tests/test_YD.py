import pytest
import requests
import configparser


class TestYD:

    def setup_method(self):
        config = configparser.ConfigParser()
        config.read('settings.ini')
        self.headers = {
            'Authorization': f'OAuth {config['YD']['token_yd']}'
        }

    @pytest.mark.parametrize(
        'param,folder_name,status_code',
        (
                ('path', 'Image', 201),
                ('path', 'Image', 409),
                ('pa', 'Music', 400),
        )
    )

    def test_create_folder(self, param, folder_name, status_code):
        params = {
            param: folder_name
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers, params=params)

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        'param,folder_name,status_code',
        (
                ('path', 'Image', 200),
                ('path', 'Image', 404),
        )
    )
    def test_check_created_folder(self, param, folder_name, status_code):
        params = {
            param: folder_name
        }
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers, params=params)

        assert response.status_code == status_code

    @pytest.mark.parametrize(
        'param,folder_name,status_code',
        (
                ('path', 'Image', 204),
                ('path', 'Image', 404),
        )
    )
    def test_delete_folder(self, param, folder_name, status_code):
        params = {
            param: folder_name
        }
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers, params=params)

        assert response.status_code == status_code