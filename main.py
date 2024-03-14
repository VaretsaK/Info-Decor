def function_info(func):
    """
    Decorator to print information about the decorated function's call.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: Decorated function.
    """
    def inner_wrapper(*args, **kwargs):
        """
        Inner wrapper function to print information before and after calling the decorated function.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.
        """
        print(f"Function '{func.__name__}' is been called with parameters: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' return this value: {result}")

        return result

    return inner_wrapper
