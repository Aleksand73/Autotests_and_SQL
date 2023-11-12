import sender_stand_request
# Шаронов Александр, 10-я когорта — Финальный проект. Инженер по тестированию плюс
def positive_assert():
    currect_track = sender_stand_request.get_order()
    assert currect_track.status_code == 200
def test_create_success_response():
    positive_assert()



