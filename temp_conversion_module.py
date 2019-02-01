def convert_c_to_f(temp_C):
    temp_F = float(temp_C)*9/5+32
    return temp_F

def main_code():
    temp_C = input("enter temperature in degC: ")
    temp_C = float(temp_C)
    temp_F = convert_c_to_f(temp_C)
    print("The temperature in {} degF".format(temp_F))

def fever_detection(temp_list):
    # max_temp = max(temp_list)
    fever_threshold = 100.5
    has_fever = False
    max_temp = 0
    for temperature in temp_list:
        if type(temperature) == str:
            temperature = float(temperature)
        if temperature > fever_threshold:
            has_fever = True
        if temperature > max_temp:
            max_temp = temperature
    return max_temp, has_fever

if __name__ == "__main__":
    main_code()
