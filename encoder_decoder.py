# FILE: encoder_decoder.py
# NAME: Encodes Or Decodes user input
# AUTHOR: Anthony Gimei
# DATE: 5/3/2018
# PURPOSE: Encodes or Decodes input string from user using certain rules
# Submission confirmation number:

# encoding A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

# Define a function for decoding
def encode(string_to_encode):
    string_to_encode = string_to_encode.upper()
    print(string_to_encode)
    encoded_string = ""

    for character in string_to_encode:
        print(character)
        counter = 0
        for letter in alpha:
            print(letter, character)
            counter += 1
            if character == letter:
                encoded_string = encoded_string + str(counter) + '-'
                break
            if character == ' ':
                encoded_string = encoded_string + ' '
                break

    return encoded_string

def decode(string_to_decode):
    string_to_decode = string_to_decode.upper()
    print(string_to_decode)
    decoded_string = ""

    for character in string_to_decode:
        print(character)
        counter = 0
        if character == '-':
                break
        else:
            for letter in alpha:
                print(letter, character)
                counter += 1
                if int(character) == counter:
                    decoded_string = decoded_string + letter
                    break
                elif character == ' ':
                    decoded_string = decoded_string + ' '
                    break


    return decoded_string

#print(encode('Anthony Gimei'))
print(decode('1-14-20-8-15-14-25- 7-9-13-5-9-'))
