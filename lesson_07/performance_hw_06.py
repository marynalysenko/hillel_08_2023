import logging
import time


class TimerContext:
    def __enter__(self):
        # Capture the start time
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        # Calculate the elapsed time
        elapsed_time = time.time() - self.start_time
        # Log the elapsed time using the logging module
        logging.info(f"Elapsed time: {elapsed_time:.2f} seconds")


# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Test the TimerContext with a sleep
# Test 1: Sleep for 1 second
with TimerContext():
    time.sleep(1)
# 2023-08-30 15:21:01,638 - INFO - Elapsed time: 1.01 seconds

# Test 2: Sleep for 0.5 seconds
with TimerContext():
    time.sleep(0.5)
# 2023-08-30 15:21:02,143 - INFO - Elapsed time: 0.51 seconds

# Test 3: Sleep for 0.1 seconds
with TimerContext():
    time.sleep(0.1)
# 2023-08-30 15:21:02,143 - INFO - Elapsed time: 0.51 seconds

# Test 4: Sleep for 3 seconds
with TimerContext():
    time.sleep(3)
# 2023-08-30 15:21:05,254 - INFO - Elapsed time: 3.01 seconds

# Test 5: No sleep (should be almost instantaneous)
with TimerContext():
    pass
# 2023-08-30 15:21:05,255 - INFO - Elapsed time: 0.00 seconds

# Test 6: List comprehension to generate a large list
with TimerContext():
    large_list = [i for i in range(1000000)]
# 2023-08-30 15:21:05,289 - INFO - Elapsed time: 0.03 seconds

# Test 7: Set comprehension to generate a large set
with TimerContext():
    large_set = {i for i in range(1000000)}
# 2023-08-30 15:21:05,328 - INFO - Elapsed time: 0.04 seconds

# Test 8: Dictionary comprehension to generate a large dictionary
with TimerContext():
    large_dict = {i: i for i in range(1000000)}
# 2023-08-30 15:21:05,370 - INFO - Elapsed time: 0.04 seconds

# Test 9: Nested loop for some computational work
with TimerContext():
    sum_val = 0
    for i in range(1000):
        for j in range(1000):
            sum_val += i * j
# 2023-08-30 15:21:05,446 - INFO - Elapsed time: 0.08 seconds

# Test 10: String operations
with TimerContext():
    s = ""
    for _ in range(100000):
        s += "test"
# 2023-08-30 15:21:05,800 - INFO - Elapsed time: 0.35 seconds

# Executing the provided test
# Test 11: Print calculation
with TimerContext():
    print(f"2+2={2+2}")
# 2023-08-30 15:21:05,800 - INFO - Elapsed time: 0.00 seconds
