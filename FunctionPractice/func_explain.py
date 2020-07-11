def get_user_data(username):
    data = {
        "naresh":{
            "age":10,
            "sex": "M",
            "city": "Blr"
        },
        "ramesh":{
            "age":20,
            "sex": "M",
            "city": "bihar"
        }
    }

    return data[username]


def employee_detail(name, company):
    company_data = {
        "Jda":{
            "ctc": "10 lpa",
            "city": "Blr"
        },
        "Tata":{
            "ctc": "10 lpa",
            "city": "Bihar"
        },
    }

    user_details = get_user_data(name)

    return {
        "company_detail": company_data[company],
        "user_detail": user_details
    }

print(employee_detail("naresh", "Jda"))