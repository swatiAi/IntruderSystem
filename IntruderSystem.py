import random
import time

# Simulating output messages with realistic temperature and humidity values
messages = [
    "System Armed",
    "Intruder detected!",
    "Fire detected!",
    "System Disarmed"
]

# Starting with System Armed
print("System Disarmed")

# Simulating the loop for fake output
for _ in range(19):  # Simulating 19 more iterations
    output = random.choice(messages)
    if "System Armed" in output or "System Disarmed" in output:
        print(output)
    elif "Intruder detected!" in output:
        print(output)
        time.sleep(1)
    elif "Fire detected!" in output:
        temperature = round(random.uniform(25.0, 35.0), 2)
        humidity = round(random.uniform(40.0, 60.0), 2)
        print(output)
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    time.sleep(1)  # Simulating a pause between messages
