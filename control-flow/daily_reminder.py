task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound  = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print()
        else:
            ...

    case 'medium':
        if time_bound == 'yes':
            print()
        else:
            ...

    case 'low':
        if time_bound == 'yes':
            print()
        else:
            ...

    case _:
        ...