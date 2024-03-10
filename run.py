import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


#...................................function to collect information from the sales
def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter sales data from the last sale day.")
        print("Information should be 6 numbers, separated by commas.")
        print("Example: 1,23,3,44,0,6\n")

        data_input = input("Enter your data here: ")    # data is comming a string value
        sales_data = data_input.split(',')              # separate our data using coma like a separator

        if check_sales_data(sales_data):                # push our info to be checked
            print("Your sales data is valid")
            break
    return sales_data

#...................................function to check information from the sales
def check_sales_data(values):
    print(values)
    try:
        [int(value) for value in values]                # convert our data type from string to integer
        if len(values) != 6:                            # check how many numbers inserted
            raise ValueError(" Is required to enter 6 numbers separated by commas", len(values))

    except ValueError as e:
        print("Wrong data entered,", e,'numbers is not enough, please try again')
        return False
    return True

#.....................................main menu...........................................

data = get_sales_data()