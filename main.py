def cavienadd(a, b):
    pass
def river():
    print("river")
    
def greet(name):
    """
    Greet a person by name.
    
    Args:
        name (str): The person's name
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}!"


def main():
    """Main function."""
    message = greet("World")
    print(message)


if __name__ == "__main__":
    main()