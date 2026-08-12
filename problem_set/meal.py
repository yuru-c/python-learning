def main():    
    time = convert(input("What time is it? ")) 

    if 7 <= time <= 8:
        print("breakfast time")  
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):    
    # hours, minutes = time.split(":")
    # if "a.m." in minutes or "p.m." in minutes:
    #     minutes, format = minutes.split(" ")
    # hours = float(hours)
    # minutes = float(minutes)
    # t = hours + minutes / 60    

    # if "p.m." in time and t < 12:
    #     t = t + 12
    # elif "a.m." in time and t >= 12:
    #     t = t - 12

    # return t


    hours, minutes = time.split(":")
    if "a.m." in minutes or "p.m." in minutes:
        minutes, period = minutes.split(" ")
    else:
        period = ""

    hours = float(hours)
    minutes = float(minutes)

    if period == "p.m." and hours != 12:
        hours += 12
    elif period == "a.m." and hours == 12:
        hours = 0

    return hours + minutes / 60

if __name__ == "__main__":
    main()