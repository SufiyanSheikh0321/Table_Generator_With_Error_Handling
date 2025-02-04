try:
    
    user_input = int(input("Enter Your Number: "))

    for num in range (1,11):
        print(f"{user_input} X {num} = {user_input*num}")

except ValueError:
    print("Error: Please enter a valid number, not a string or special character..!")