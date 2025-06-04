def greet(name):
    """Greet the user with a message."""
    print(f"Hello, {name}! Welcome to myapp.")
    return f"Hello, {name}!"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        greet(sys.argv[1])
    else:
        greet("User")