
from datetime import timedelta, datetime


def display_current_datetime():
    current_date = datetime.now()
    return current_date


def main():
    current_date = display_current_datetime()
    print(f"Current date and time:{current_date}")
    add_days = int(input("Enter the number of days to add to the current date: "))
    future_date=current_date + timedelta(days=add_days)
    print(f'Future date:{future_date.strftime('%Y-%m-%d %H:%M:%S')}')



if __name__ == "__main__":
    main()