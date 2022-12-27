from utils.http_methods import HttpMethods


base_url = "https://rahulshettyacademy.com/"
key = "?key=qaclick123"


class GoogleMapsAPI:

    @staticmethod
    def post_location():

        json_post_location = {"location": {"lat": -38.383494, "lng": 33.427362}, "accuracy": 50,
                             "name": "Frontline house", "phone_number": "(+91) 983 893 3937",
                             "address": "29, side layout, cohen 09", "types": ["shoe park", "shop"],
                             "website": "http://google.com", "language": "French-IN"}

        post_resource = "maps/api/place/add/json"
        post_url = base_url + post_resource + key
        result_post = HttpMethods.post(post_url, json_post_location)

        return result_post

    @staticmethod
    def get_location(place_id):

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        result_get = HttpMethods.get(get_url)

        return result_get

    @staticmethod
    def put_location(place_id):
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key

        json_put_location = {"place_id": place_id, "address": "100 Lenina street, RU", "key": "qaclick123"}

        result_put = HttpMethods.put(put_url, json_put_location)

        return result_put

    @staticmethod
    def delete_location(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key

        json_delete_location = {"place_id": place_id}

        result_delete = HttpMethods.delete(delete_url, json_delete_location)

        return result_delete



