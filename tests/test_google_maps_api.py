import allure
from utils.api import GoogleMapsAPI
from utils.asserts import Checking


@allure.epic("Test create location")
class TestCreateLocation:

    @allure.description("Test create, update and delete location")
    def test_create_new_location(self):
        result_post = GoogleMapsAPI.post_location()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_values(result_post, 'status', 'OK')

        result_get = GoogleMapsAPI.get_location(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_values(result_get, 'address', '29, side layout, cohen 09')

        result_put = GoogleMapsAPI.put_location(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_values(result_put, 'msg', 'Address successfully updated')

        result_get = GoogleMapsAPI.get_location(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_values(result_get, 'address', '100 Lenina street, RU')

        result_delete = GoogleMapsAPI.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_values(result_delete, 'status', 'OK')

        result_get = GoogleMapsAPI.get_location(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_part_values(result_get, 'msg', 'Get operation failed')
