from scheduler import schedule_shutdown, cancel_shutdown
from utils import validate_time


def main():
    print("=== TimeOut ===")
    print("1 - Schedule shutdown")
    print("2 - Cancel shutdown")

    option = input("Choose an option: ").strip()

    if option == "1":
        target_time = input("Enter time (HH:MM): ").strip()

        if not validate_time(target_time):
            print("Invalid time format. Use HH:MM.")
            return

        seconds = schedule_shutdown(target_time)
        print(f"Shutdown scheduled successfully. Time remaining: {seconds} seconds.")
    elif option == "2":
        cancel_shutdown()
        print("Shutdown canceled.")
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()

    