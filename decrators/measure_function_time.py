""" measure the time a function takes to execture
"""
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1 return the float value of time in seconds
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
        
"""
 If you want to do more precise measurements of code, 
 you should instead consider the timeit module in the standard library. 
 It temporarily disables garbage collection and runs multiple trials to strip out noise from quick function calls.
 """
