"""
Base62 Encoding and Decoding

Base62 uses 62 characters: 0-9, a-z, A-Z
Commonly used for URL shortening and compact number representation.
"""

class Base62:
    """Base62 encoder/decoder class"""
    
    # Character set: 0-9 (10) + a-z (26) + A-Z (26) = 62 characters
    CHARSET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = len(CHARSET)
    
    @classmethod
    def encode(cls, number: int) -> str:
        """
        Encode an integer to base62 string
        
        Args:
            number (int): Non-negative integer to encode
            
        Returns:
            str: Base62 encoded string
            
        Raises:
            ValueError: If number is negative
        """
        if not isinstance(number, int):
            raise TypeError("Input must be an integer")
        
        if number < 0:
            raise ValueError("Number must be non-negative")
        
        if number == 0:
            return cls.CHARSET[0]
        
        result = []
        while number > 0:
            remainder = number % cls.BASE
            result.append(cls.CHARSET[remainder])
            number //= cls.BASE
        
        return ''.join(reversed(result))
    
    @classmethod
    def decode(cls, encoded_str: str) -> int:
        """
        Decode a base62 string to integer
        
        Args:
            encoded_str (str): Base62 encoded string
            
        Returns:
            int: Decoded integer
            
        Raises:
            ValueError: If string contains invalid characters
        """
        if not isinstance(encoded_str, str):
            raise TypeError("Input must be a string")
        
        if not encoded_str:
            raise ValueError("Input string cannot be empty")
        
        result = 0
        for char in encoded_str:
            if char not in cls.CHARSET:
                raise ValueError(f"Invalid character '{char}' in base62 string")
            
            digit_value = cls.CHARSET.index(char)
            result = result * cls.BASE + digit_value
        
        return result


def demo_base62():
    """Demonstration of Base62 encoding and decoding"""
    print("=== Base62 Encoding/Decoding Demo ===\n")
    
    # Test cases
    test_numbers = [0, 1, 61, 62, 100, 1000, 12345, 987654321, 2**32 - 1]
    
    print("Number -> Encoded -> Decoded")
    print("-" * 35)
    
    for num in test_numbers:
        encoded = Base62.encode(num)
        decoded = Base62.decode(encoded)
        print(f"{num:>10} -> {encoded:>8} -> {decoded:>10}")
        
        # Verify round-trip conversion
        assert num == decoded, f"Round-trip failed for {num}"
    
    print("\n✅ All round-trip tests passed!")
    
    # Test string examples
    print("\n=== String Examples ===")
    test_strings = ["a", "Z", "10", "abc", "Hello", "Base62Test"]
    
    print("String -> Decoded -> Re-encoded")
    print("-" * 35)
    
    for s in test_strings:
        try:
            decoded = Base62.decode(s)
            re_encoded = Base62.encode(decoded)
            print(f"{s:>10} -> {decoded:>8} -> {re_encoded:>10}")
        except ValueError as e:
            print(f"{s:>10} -> ERROR: {e}")


def test_error_handling():
    """Test error handling for invalid inputs"""
    print("\n=== Error Handling Tests ===")
    
    # Test invalid encode inputs
    print("Testing encode with invalid inputs:")
    invalid_encode_inputs = [-1, -100, "string", 3.14, None]
    
    for inp in invalid_encode_inputs:
        try:
            result = Base62.encode(inp)
            print(f"  {inp} -> {result} (unexpected success)")
        except (ValueError, TypeError) as e:
            print(f"  {inp} -> ERROR: {e} ✅")
    
    # Test invalid decode inputs
    print("\nTesting decode with invalid inputs:")
    invalid_decode_inputs = ["", "invalid@char", "spaces here", None, 123]
    
    for inp in invalid_decode_inputs:
        try:
            result = Base62.decode(inp)
            print(f"  {inp} -> {result} (unexpected success)")
        except (ValueError, TypeError) as e:
            print(f"  '{inp}' -> ERROR: {e} ✅")


def benchmark_base62():
    """Simple benchmark of encoding/decoding operations"""
    import time
    
    print("\n=== Performance Benchmark ===")
    
    # Test with a range of numbers
    test_range = range(100000)
    
    # Benchmark encoding
    start_time = time.time()
    encoded_values = [Base62.encode(i) for i in test_range]
    encode_time = time.time() - start_time
    
    # Benchmark decoding
    start_time = time.time()
    decoded_values = [Base62.decode(encoded) for encoded in encoded_values]
    decode_time = time.time() - start_time
    
    # Verify correctness
    assert list(test_range) == decoded_values
    
    print(f"Encoded {len(test_range)} numbers in {encode_time:.3f}s")
    print(f"Decoded {len(encoded_values)} strings in {decode_time:.3f}s")
    print(f"Average encode time: {encode_time/len(test_range)*1000:.3f}ms per number")
    print(f"Average decode time: {decode_time/len(encoded_values)*1000:.3f}ms per string")


def interactive_mode():
    """Interactive mode for user input"""
    print("\n=== Interactive Mode ===")
    print("Commands:")
    print("  encode <number>  - Encode a number to base62")
    print("  decode <string>  - Decode a base62 string to number")
    print("  quit            - Exit interactive mode")
    
    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            parts = user_input.split()
            if len(parts) != 2:
                print("Invalid command. Use 'encode <number>' or 'decode <string>'")
                continue
            
            command, value = parts[0].lower(), parts[1]
            
            if command == 'encode':
                try:
                    num = int(value)
                    encoded = Base62.encode(num)
                    print(f"Encoded: {encoded}")
                except ValueError:
                    print("Invalid number. Please enter a non-negative integer.")
            
            elif command == 'decode':
                try:
                    decoded = Base62.decode(value)
                    print(f"Decoded: {decoded}")
                except ValueError as e:
                    print(f"Error: {e}")
            
            else:
                print("Unknown command. Use 'encode' or 'decode'")
                
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            break


if __name__ == "__main__":
    # Run all demonstrations
    demo_base62()
    test_error_handling()
    benchmark_base62()
    
    # Optional interactive mode
    print("\nWould you like to try interactive mode? (y/n)")
    if input().strip().lower() in ['y', 'yes']:
        interactive_mode()
    
    print("\nBase62 demonstration complete!")
