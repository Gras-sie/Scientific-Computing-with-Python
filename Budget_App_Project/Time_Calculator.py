def add_time(start, duration, starting_day=None):
    # List of days for reference, used if starting_day is provided
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Split the start time string into time and AM/PM meridian
    time, meridian = start.split()
    # Split the time part into hour and minute, and convert them to integers
    hour, minute = map(int, time.split(':'))

    # Convert start time to 24-hour format for easier calculation
    # If it's PM and not 12 PM (noon), add 12 hours
    if meridian == "PM" and hour != 12:
        hour += 12
    # If it's AM and 12 AM (midnight), set hour to 0
    elif meridian == "AM" and hour == 12:
        hour = 0

    # Calculate the total start time in minutes from midnight
    start_minutes = hour * 60 + minute

    # Parse the duration string into hours and minutes
    dur_hours, dur_minutes = map(int, duration.split(':'))
    # Calculate the total duration in minutes
    dur_total_minutes = dur_hours * 60 + dur_minutes

    # Calculate the total end time in minutes from the start day's midnight
    end_minutes = start_minutes + dur_total_minutes

    # Calculate how many full 24-hour periods (days) have passed
    total_days = end_minutes // (24 * 60)
    # Calculate the remaining minutes within the final day
    remaining_minutes = end_minutes % (24 * 60)
    # Calculate the final hour in 24-hour format from the remaining minutes
    final_hour_24 = remaining_minutes // 60
    # Calculate the final minute from the remaining minutes
    final_minute = remaining_minutes % 60

    # Convert the final hour back to 12-hour format
    # Determine if it's AM or PM based on the 24-hour final hour
    meridian = "AM" if final_hour_24 < 12 else "PM"
    # Convert 24-hour to 12-hour format (e.g., 13:00 becomes 1:00 PM, 00:00 becomes 12:00 AM)
    final_hour_12 = final_hour_24 % 12
    # If the 12-hour format results in 0 (e.g., 00:xx or 12:xx), set it to 12
    if final_hour_12 == 0:
        final_hour_12 = 12

    # Build the new time string in HH:MM AM/PM format
    new_time = f"{final_hour_12}:{final_minute:02d} {meridian}"

    # Handle the day of the week if a starting day was provided
    if starting_day:
        # Find the index of the starting day (case-insensitive)
        index = days.index(starting_day.capitalize())
        # Calculate the new day by adding total_days passed, modulo 7 for week cycle
        new_day = days[(index + total_days) % 7]
        # Append the new day to the time string
        new_time += f", {new_day}"

    # Add information about the number of days passed
    # If exactly one day has passed
    if total_days == 1:
        new_time += " (next day)"
    # If more than one day has passed
    elif total_days > 1:
        new_time += f" ({total_days} days later)"

    # Return the final formatted time string
    return new_time
