MEAN_PER_TRIP = 9.72
STANDARD_DEVIATION_PER_TRIP = 3.125
AVERAGE_NUM_TRIPS = 3.7845
# data taken from http://nhts.ornl.gov/tables09/fatcat/2009/avtl_WHYTRP1S.html
# and http://nhts.ornl.gov/det/Extraction4.aspx

MILEAGE_TYPES = {"LOW":    0,
                 "MEDIUM": (MEAN_PER_TRIP - STANDARD_DEVIATION_PER_TRIP) * AVERAGE_NUM_TRIPS,
                 "HIGH":   (MEAN_PER_TRIP + STANDARD_DEVIATION_PER_TRIP) * AVERAGE_NUM_TRIPS}
# MILEAGE_TYPES are the classifications based on how many miles per day.

MEAN_TIME_PER_TRIP = 19.1
STANDARD_DEVIATION_TIME_PER_TRIP = 20.3
# Data taken from http://nhts.ornl.gov/2009/pub/stt.pdf p37

TIME_TYPES = {"LOW":    0,
              "MEDIUM": (MEAN_TIME_PER_TRIP - STANDARD_DEVIATION_TIME_PER_TRIP / 2) * AVERAGE_NUM_TRIPS,
              "HIGH":   (MEAN_TIME_PER_TRIP + STANDARD_DEVIATION_TIME_PER_TRIP / 2) * AVERAGE_NUM_TRIPS}
# TIME_TYPES are the classifications based on how many minutes per day.

TYPE_VALUES = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}


def classify(mileage, time, return_as_string=True):
    """Returns the category of driver someone falls into."""
    
    mile_type = time_type = None

    if mileage < MILEAGE_TYPES["MEDIUM"]:
        mile_type = "LOW"
    elif mileage < MILEAGE_TYPES["HIGH"]:
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
    
    """Format: (MILEAGE, TIME) 
    0 - LOW LOW
    1 - LOW MEDIUM
    2 - LOW HIGH
    3 - MEDIUM LOW
    4 - MEDIUM MEDIUM
    5 - MEDIUM HIGH
    6 - HIGH LOW
    7 - HIGH MEDIUM
    8 - HIGH HIGH
    """

if __name__ == "__main__":
    print classify(15, 30, False)
    print classify(50, 125, False)
    print classify(15, 30)
    print classify(50, 125)

