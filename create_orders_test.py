# Айгуль Вакилова, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def get_orders():
    response = sender_stand_request.post_new_order(data.order_body_response)
    track = response.json()["track"]
    response = sender_stand_request.get_order(track)

    assert response.status_code == 200

#Тест получения данных о заказе
def test_get_orders():
    get_orders()