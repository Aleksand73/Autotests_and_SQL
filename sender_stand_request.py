import configuration
import requests
import data
# Шаронов Александр, 10-я когорта — Финальный проект. Инженер по тестированию плюс
def post_new_order(body):
      return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)
response = post_new_order(data.orders_body);
print(response.status_code)
print(response.json())

def get_saved_track():
    new_saved_track = post_new_order(data.orders_body)
    return new_saved_track.json()['track']

def get_order():
    currect_track = get_saved_track()
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PATH,
                            params={'t': currect_track})
response = get_order();
print(response.status_code)
print(response.json())












