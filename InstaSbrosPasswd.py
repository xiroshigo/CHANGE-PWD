from uuid import uuid4
from requests import post


def target():
    global username
    username = input("\033[1;32mFoydalanivchi nomi  '@' belgisisiz yozing: \033[1;36m")
    if username[0] == '@':
        print("\n\n\033[1;31miltimos bu bn emas'@'")
        target()

    url_target = "https://i.instagram.com/api/v1/users/lookup/"

    header_target = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
    }

    data_target = {

        "phone_id": uuid4(),
        "q": username,
        "guid": uuid4(),
        "device_id": uuid4(),
        "android_build_type": "release",
        "waterfall_id": uuid4(),
        "directly_sign_in": "true",
        "is_wa_installed": "false"
    }

    req_target = post(url=url_target, headers=header_target, data=data_target)

    try:
        if '"user":{"pk"' not in req_target.text:
            user_id = req_target.json()["user"]["pk"]
            print("\033[1;31m user_id  Topilmadi")

        elif '"can_email_reset":true' and '"can_sms_reset":true' in req_target.text:
            choose = input("""\033[1;32m
[1]\033[1;36m Emailga yuborish
\033[1;32m[2]\033[1;36m Telefon raqamiga yuborish
\033[1;32m[*]\033[1;33m Menulardan birini yozing: \033[1;32m""")

            if choose == "1":
                send_email()
            elif choose == "2":
                send_phone()

        elif '"can_email_reset":true' in req_target.text:
            send_email()

        elif '"can_sms_reset":true' in req_target.text:
            send_phone()

        else:
            input(req_target.text)
    except:
        input("\033[1;31mQayta urinishdan oldin bir necha daqiqa kuting.")


def send_email():
    url_send_email = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"

    header_send_email = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
    }

    data_send_email = {

        "adid": uuid4(),
        "query": username,
        "guid": uuid4(),
        "device_id": uuid4(),
        "waterfall_id": uuid4()
    }

    req_send_email = post(url=url_send_email, headers=header_send_email, data=data_send_email)
    if "email" in req_send_email.text:
        email = req_send_email.json()["email"]
        print(f"\033[1;32memailga jonatildi {email}\033[1;36m")


def send_phone():
    url_send_phone = "https://i.instagram.com/api/v1/users/lookup_phone/"

    header_send_phone = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
    }

    data_send_phone = {

        "supports_sms_code": "true",
        "guid": uuid4(),
        "device_id": uuid4(),
        "query": username,
        "android_build_type": "release",
        "waterfall_id": uuid4(),
        "use_whatsapp": "false"
    }

    req_send_phone = post(url=url_send_phone, headers=header_send_phone, data=data_send_phone)
    if "phone_number" in req_send_phone.text:
        phone_number = req_send_phone.json()["phone_number"]
        print(f"\033[1;32mLink telefon raqamiga jonatildi {phone_number}\033[1;36m")


if __name__ == "__main__":
    print(f"""
\033[1;35m
 _______  __   __  _______  __    _  _______  _______  _______  _     _  ______  
|       ||  | |  ||   _   ||  |  | ||       ||       ||       || | _ | ||      | 
|       ||  |_|  ||  |_|  ||   |_| ||    ___||    ___||    _  || || || ||  _    |
|       ||       ||       ||       ||   | __ |   |___ |   |_| ||       || | |   |
|      _||       ||       ||  _    ||   ||  ||    ___||    ___||       || |_|   |
|     |_ |   _   ||   _   || | |   ||   |_| ||   |___ |   |    |   _   ||       |
|_______||__| |__||__| |__||_|  |__||_______||_______||___|    |__| |__||______| 
    
\033[1;33m    
[+] Instagram parolini oʻchirish uchun termux terminali tooliga hush kelibsiz\nDasturchi: \033[1;31m@red_uzbek \033[1;33m[+]\n\n\n""")
    target()