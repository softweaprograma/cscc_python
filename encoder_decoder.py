# FILE: encoder_decoder.py
# NAME: Encodes Or Decodes user input
# AUTHOR: Anthony Gimei
# DATE: 5/3/2018
# PURPOSE: Encodes or Decodes input string from user using certain rules
# Submission confirmation number:

# encoding A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,T=20,U=21,V=22,W=23,X=24,Y=25,Z=26
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Define a function for decoding
def encode(word_to_encode):
    word_to_encode = word_to_encode.upper()
    print(word_to_encode)
    encoded_name = ""

    for character in word_to_encode:
        print(character)
        counter = 0
        for letter in alpha:
            print(letter,character)
            counter += 1
            if character == letter:
                encoded_name = encoded_name + str(counter) + '-'
                break
            if character == ' ':
                encoded_name = encoded_name + ' '
                break

    return encoded_name

print(encode('Anthony Gimei'))

