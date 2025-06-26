from alphabet_caesar import alphabet
from art_caesar import logo

print(logo)
print("**************************Welcome to Python Caesar Cipher**************************")


def caesar(original_text, shift_amount, encode_or_decode):
    chiper_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1  #because need - shift_amount to decrypt

    for letter in original_text:

        if letter not in alphabet:
            chiper_text += letter
        else:

            shifted_position = alphabet.index(letter)+shift_amount #encrypt
            shifted_position %= len(alphabet)
            chiper_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {chiper_text}")

repeat_encode_decode = True

while repeat_encode_decode:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to continue encode/decode, Type 'no' if you want to Goodbye: ").lower()

    if restart == "no":
        repeat_encode_decode = False
    print("Good Byee!")


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
######################################################################################################################
# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
