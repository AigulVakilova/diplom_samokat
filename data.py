headers = {
    "Content-Type": "application/json"
}

order_body_response = {
    "firstName": "Марина",
    "lastName": "Воронина",
    "address": "Гагарина, 35",
    "metroStation": 200,
    "phone": "+7 922 355 35 35",
    "rentTime": 4,
    "deliveryDate": "2023-09-20",
    "comment": "Позвонить заранее",
    "color": [
        "BLACK"
    ]
}

order_body_request = {
    "order": {
        "id": 1,
        "firstName": "Анастасия",
        "lastName": "Сорокина",
        "address": "Южная, 50",
        "metroStation": "208",
        "phone": "+79557784438",
        "rentTime": 4,
        "deliveryDate": "2023-09-18T00:00:00.000Z",
        "track": 816950,
        "color": [
            "BLACK"
        ],
        "comment": "Позвонить заранее",
        "cancelled": False,
        "finished": False,
        "inDelivery": False,
        "createdAt": "2023-09-16T17:51:17.085Z",
        "updatedAt": "2023-09-16T17:51:17.085Z",
        "status": 0
    }
}