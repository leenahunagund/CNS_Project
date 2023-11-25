import gradio as gr

# This function generates the key in a cyclic manner until its length isn't equal to the length of the original text
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# This function returns the encrypted text generated with the help of the key
def cipherText(string, key):
    string = string.upper()
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord("A")
        cipher_text.append(chr(x))
    return "".join(cipher_text)

# This function decrypts the encrypted text and returns the original text
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord("A")
        orig_text.append(chr(x))
    orig_text = "".join(orig_text)
    orig_text = orig_text.lower()
    return orig_text

# Define Gradio interface
iface = gr.Interface(
    fn=lambda string, key: [cipherText(string, generateKey(string, key)),
                            originalText(cipherText(string, generateKey(string, key)), generateKey(string, key))],
    inputs=["text", "text"],
    outputs=[
        gr.Textbox(placeholder="Ciphertext will appear here", label="Ciphertext"),
        gr.Textbox(placeholder="Original Text will appear here", label="Original Text"),
    ],
)

# Launch the Gradio interface
iface.launch()
