# import os


# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')


# # Example usage
# print("Some text before clearing.")
# input("Press Enter to clear the screen...")
# clear_screen()
# print("Some text after clearing.")

# Fuctions with output
# def multiply():
#     return 3*2


# output = multiply()
# print(output)


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"


# print(format_name("angela", "yu"))

year = int(input("Enter the year :"))
month = int(input("Enter the month :"))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month-1]


days = days_in_month(year, month)
print(days)
