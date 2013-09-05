#!/usr/bin/env python
# -*- "coding": utf-8 -*-


def get_cab_driver(
        driver_pk, device="ios", simple_status="available", status="unknown", is_coa=False,
        is_arrived_waiting=False, is_drop=False, drop_minutes=None, is_on_way_to_job=False, is_end_of_shift=False,
        is_on_a_break=False, is_flag_down=False, is_passenger_on_board=False):
    doc = {
        "_id": {
            "$oid": driver_pk
        },
        "accepts_mandatory_dispatch": False,
        "active": True,
        "address1": "Chatham Street",
        "address2": "London",
        "auth_token": "700289451310",
        "bio": "I've been in the industry for 20 years and am a safe driver",
        "city": "SE17",
        "country": {
            "code": "GB",
            "_db_storage": "locations_country"
        },
        "active_vehicle": None,
        "current_device": {
            "sandbox": False,
            "tracking_engine": "api",
            "current": True,
            "app_in_background": True,
            "token": "f6eb97469b381bdf11e573627dcf0d76ad9bced40cb17e401613072f2b2da597",
            "diagnostics": [
                "ping-pong",
                "push-confirmation"
            ],
            "type": "ios"
        },
        "daily_wage": 100,
        "date_joined": None,
        "date_license_expire": None,
        "date_of_birth": {
        },
        "device_token": None,
        "device_type": device,
        "driver_license_number": "",
        "email": "lee@democars.co.uk",
        "gender": "male",
        "home_phone": "",
        "insurance_expire_date": None,
        "insurance_premium": 0,
        "joined_offices_pks": [
        ],
        "last_application_name": "Driver Android",
        "last_application_version": "2013071500",
        "last_device_unregistration": {
        },
        "last_location_update": {
        },
        "last_log_hash": "97c2bf0cfcb567a719dd317e9315b74a",
        "last_requested_mobile_api_version": "2",
        "last_substatus_change_time": {
        },
        "license_class": "",
        "location": {
            "lng": -3.9520797391741835,
            "lat": 51.62087270475762
        },
        "location_latitude": 65.5782763241,
        "location_longitude": 22.2022841871,
        "mobile_settings": None,
        "modified_date": {
        },
        "mot_expire_date": None,
        "name": "James Lee",
        "national_insurance_number": "XX 00 00 00 X",
        "nationality": "Chinese",
        "nickname": "Lee",
        "office": None,
        "offline": True,
        "password": "sha1$EIQUHFYBkjZV$9bba7548b1c3c9a865e082ee499822f7945d406a",
        "pco_expire_driver": None,
        "pco_number": "",
        "penalty_points": 0,
        "phone": "+44987654321",
        "phv_license": "",
        "postcode": "United Kingdom",
        "price_per_mile": 0,
        "price_rule": "",
        "profile_photo": None,
        "receive_dispatched_booking_email": True,
        "receive_dispatched_booking_sms": False,
        "receives_notifications_in_device": True,
        "road_tax_expire": None,
        "sequential": 4,
        "simple_status": simple_status,
        "status": status,
        "sub_status": {
            "is_coa": is_coa,
            "is_arrived_waiting": is_arrived_waiting,
            "is_drop": is_drop,
            "is_on_way_to_job": is_on_way_to_job,
            "is_end_of_shift": is_end_of_shift,
            "is_on_a_break": is_on_a_break,
            "is_flag_down": is_flag_down,
            "is_passenger_on_board": is_passenger_on_board
        },
        "tracking_engine": "api",
        "tracking_entity_id": "",
        "username": "james"
    }

    if drop_minutes is not None:
        doc["sub_status"]['drop_minutes'] = drop_minutes

    return doc
