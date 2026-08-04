import base62

if __name__ == "__main__":    
    print("Base62 Encoding/Decoding:")
    for num in range(0, 1000000000):
        encoded = encode(num)
        decoded = decode(encoded)
        print(f"{num} -> {encoded}")
