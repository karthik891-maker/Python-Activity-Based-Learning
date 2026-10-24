text = input("Enter text to compress: ")
if text == "":
    print("Empty input; nothing to encode.")
else:
    encoded = ""
    current = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current:
            count += 1
        else:
            encoded += current + str(count)
            current = text[i]
            count = 1
    encoded += current + str(count)
    print("Encoded text:", encoded)
    print("Original length:", len(text))
    print("Encoded length:", len(encoded))
    if len(encoded) < len(text):
        print("Compression is beneficial.")
    else:
        print("Compression is not beneficial.")
