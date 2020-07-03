def mysum(a, b):
    if __name__ == "app":
        print("NAreshhhhhhhhhhh")

    return a + b


def get_user_data(user):
    data = {
        "Naresh" : {
            "age" : 24,
            "city" : "Bangalore"
        },
        "Megha" : {
            "age" : 60,
            "city" : "Delhi"
        },
        "Deepak" : {
            "age" : 80,
            "city" : "Kapurthala"
        }
    }
    return data.get(user)

print(__name__)
