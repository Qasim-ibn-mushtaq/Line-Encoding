# Function to encode data using a generic encoding scheme (e.g., NRZ, RZ, etc.)
def encode_data(data, encoding_scheme):
    # Implement the encoding logic for the chosen scheme
    encoded_signal = encoding_scheme(data)
    return encoded_signal

# Function to decode data using a generic decoding scheme (e.g., NRZ, RZ, etc.)
def decode_data(encoded_signal, decoding_scheme):
    # Implement the decoding logic for the chosen scheme
    decoded_data = decoding_scheme(encoded_signal)
    return decoded_data

# Sample encoding and decoding schemes
def nrz_encoding(data):
    # Implement NRZ encoding logic here
    pass

def nrz_decoding(encoded_signal):
    # Implement NRZ decoding logic here
    pass

# Sample data for testing
data = [0, 1, 0, 1, 1, 0, 0, 1]

# Choose encoding and decoding schemes
encoding_scheme = nrz_encoding
decoding_scheme = nrz_decoding

# Encode the data using the chosen encoding scheme
encoded_signal = encode_data(data, encoding_scheme)

# Display the encoded signal
print("Encoded Signal:", encoded_signal)

# Ask the user if they want to decode the signal
user_input = input("Do you want to decode the signal (yes/no)? ")

if user_input.lower() == "yes":
    # Decode the signal using the chosen decoding scheme
    decoded_data = decode_data(encoded_signal, decoding_scheme)

    if decoded_data is not None:
        # Display the decoded data
        print("Decoded Data:", decoded_data)
