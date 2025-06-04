from myapp.main import greet

def test_greet():
    result = greet("Raj")
    assert result == "Hello, Raj!"
    print("Test passed: greet function works correctly.")

if __name__ == "__main__":
    test_greet()