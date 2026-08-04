# Simple Base62 encoding and decoding

CHARSET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode(number):
    """Convert integer to base62 string"""
    if number == 0:
        return "0"
    
    result = ""
    while number > 0:
        result = CHARSET[number % 62] + result
        number //= 62
    
    return result

def decode(encoded_str):
    """Convert base62 string to integer"""
    result = 0
    for char in encoded_str:
        result = result * 62 + CHARSET.index(char)
    return result

if __name__ == "__main__":    
    print("Base62 Encoding/Decoding:")
    for num in range(0, 1000000000):
        encoded = encode(num)
        decoded = decode(encoded)
        print(f"{num} -> {encoded}")
