MILEAGE_TYPES = {"LOW": 0,
                 "MEDIUM": 50,
                 "HIGH": 100}
# MILEAGE_TYPES are the classifications based on how many miles per day.

TIME_TYPES = {"LOW": 0, "MEDIUM": 2, "HIGH": 4}
# TIME_TYPES are the classifications based on how many hours per day.

TYPE_VAULES = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}

def what_type(mileage, time, return_as_string=True):
    """Returns the category of driver someone falls into."""
    
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

    if return_as_string:
        return mile_type, time_type
    else:
        # This should return a different number for each type pair
        return TYPE_VALUES[mile_type] * 3 + TYPE_VALUES[time_type]
