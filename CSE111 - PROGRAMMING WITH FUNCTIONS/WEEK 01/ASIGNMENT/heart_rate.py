
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

user_age = input("\nPlease enter your age: ")
user_age = int(user_age)

maximum_heart_rate = 220 - user_age

slowest_rates = 65/100 * maximum_heart_rate

fastest_beats = 85/100 * maximum_heart_rate

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {slowest_rates:.0f} and {int(fastest_beats)} beats per minute.")
print()