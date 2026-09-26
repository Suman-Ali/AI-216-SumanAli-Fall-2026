# Problem: Classify AI service response times
# Inputs: list of response times in milliseconds
# Rules: Fast <= 300, Acceptable 301-700, Slow > 700
# Repetition: loop through all response times
# Outputs: category for each time and final summary

response_times = [250, 420, 180, 900, 310, 1500, 275]

fast = 0
acceptable = 0
slow = 0

for time in response_times:
    if time <= 300:
        print(f"{time}ms → Fast")
        fast += 1
    elif time <= 700:
        print(f"{time}ms → Acceptable")
        acceptable += 1
    else:
        print(f"{time}ms → Slow")
        slow += 1

print("\n--- Summary ---")
print(f"Fast: {fast}")
print(f"Acceptable: {acceptable}")
print(f"Slow: {slow}")