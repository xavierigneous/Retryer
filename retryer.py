import functools
import time

def retryer(max_retries, delay, on_error=None):
    # Params:
    # * max_retries: The maximum number of times the function should be retried on error.
    # * retry_delay: The delay in seconds between retry attempts.
    # * on_error: A custom error handling function that will be executed when an error occurs.
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = 0
            while retry_count < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"ERROR: Function {func.__name__} raised an error: {e}")
                    on_error(e)
                    retry_count += 1
                    if retry_count == max_retries:
                        print(
                            f"Function {func.__name__} failed after {max_retries} retries. Moving to the next function.")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator
