MILEAGE_TYPES = {"LOW": 0,
                 "MEDIUM": 50,
                 "HIGH": 100}
# MILEAGE_TYPES are the classifications based on how many miles per day.

TIME_TYPES = {"LOW": 0, "MEDIUM": 2, "HIGH": 4}
# TIME_TYPES are the classifications based on how many hours per day.

def what_type(mileage, time):
    mile_type = time_type = None
    if mileage < MILEAGE_TYPES["MEDIUM"]:
        mile_type = "LOW"
    elif mileage < MILEAGE_TYPE["HIGH"]:
        mile_type = "MEDIUM"
    else:
        mile_type = "HIGH"

    if time < TIME_TYPES["MEDIUM"]:
        time_type = "LOW"
    elif time < TIME_TYPES["HIGH"]:
        time_type = "MEDIUM"
    else:
        time_type = "HIGH"

    return mile_type, time_type
