""" Write a function that gets the time as three integer arguments (for hours, minutes, and 
seconds) and returns the number of seconds since the last time the clock “reached 12.” 
Use this function to calculate the amount of time in seconds between two hours, 
when both are within a 12-hour cycle. """


def cal_seconds(hours, minutes, seconds):
    """Calculate the total seconds of given input time since the last time the clock 'reached 12'"""

    total_seconds  = ((hours*60) + minutes)*60 + seconds
    return total_seconds

def main():
    hours = int(input("Enter Time in\nhours    :"))
    minutes = int(input("minutes  :"))
    seconds = int(input("seconds  :"))

    if hours>=0 and hours<12 and minutes>=0 and minutes<60 and seconds>=0 and seconds<60:
        total_seconds = cal_seconds(hours, minutes, seconds)
        print("the total number of seconds is", total_seconds)
    else:
        print("Please enter valid inputs (hours, minutes, seconds) in 12-hour cycle")
        main()
    
if __name__ == "__main__":
    main()