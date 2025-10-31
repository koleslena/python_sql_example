import time

def benchmark(func):
    """Wrapper for benchmarking."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.6f} seconds")
        return result
    return wrapper