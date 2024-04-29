import re

def parse_time(input_time):
    # Regular expression to extract hours, minutes, and seconds from the input string
    time_pattern = re.compile(r'(\d+) hours?, (\d+) minutes?, (\d+) seconds?')
    match = time_pattern.match(input_time)
    if match:
        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        return hours, minutes, seconds
    else:
        raise ValueError("Invalid input format")

def format_time(hours, minutes, seconds):
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def divide_time(input_time, divisor):
    hours, minutes, seconds = parse_time(input_time)
    
    # Convert everything to seconds for easier manipulation
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    # Divide by the divisor
    divided_seconds = total_seconds // divisor
    
    # Convert back to hours, minutes, and seconds
    new_hours = divided_seconds // 3600
    divided_seconds %= 3600
    new_minutes = divided_seconds // 60
    new_seconds = divided_seconds % 60
    
    return format_time(new_hours, new_minutes, new_seconds)

# Example usage
input_time = input('Input time: ')
divisor = int(input('Input divisor: '))
result = divide_time(input_time, divisor)
print("Divided time:", result)