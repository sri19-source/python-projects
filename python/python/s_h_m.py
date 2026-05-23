#conversion of seconds to hours, minutes and seconds
def convert_seconds(seconds):
    hours = seconds // 3600#so first it divides therefore hours are calculated then it calculates 
    minutes = (seconds % 3600) // 60
    #the remaining seconds and divides by 60 to get minutes and then the remaining seconds are calculated by taking modulus of 60
    remaining_seconds = seconds % 60

    return hours, minutes, remaining_seconds

#taking input from user
total_seconds = int(input("Enter the total number of seconds: "))
hours, minutes, seconds = convert_seconds(total_seconds)
#printing the result
print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
