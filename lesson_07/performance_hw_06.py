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

# Test 2: Sleep for 0.5 seconds
with TimerContext():
    time.sleep(0.5)

# Test 3: Sleep for 0.1 seconds
with TimerContext():
    time.sleep(0.1)

# Test 4: Sleep for 3 seconds
with TimerContext():
    time.sleep(3)

# Test 5: No sleep (should be almost instantaneous)
with TimerContext():
    pass
