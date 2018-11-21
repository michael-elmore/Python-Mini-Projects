# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 21:43:45 2018

@author: Michael
"""

"""
This is a set of functions that simulates the ENIGMA machine
with encoding and decoding functions.
"""

import random

daykey = ["CXA",(rotor1, rotor2, rotor3),"KSMVBECHJDWPTNZIUYXA"]

samplemessage = "IUSEDTOLOVEKASIAKORYZMAIWONDERIFIWOULDLIKEHERTODAYASMUCHASIDIDALLTHOSEYEARSAGO"

def scrambleGenerator():
    # This generates a string that represents the scramble
    # sequence. It can then be used to simulate ENIGMA rotors
    # or the reflector by either moving up or down it.
    scrambled = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while len(scrambled) < 26:
        num = random.randint(0, len(alphabet))
        nextletter = alphabet[num-1]
        while nextletter in scrambled:
            num = random.randint(0, len(alphabet))
            nextletter = alphabet[num-1]
        scrambled += nextletter
    return scrambled

def offsetCalculator(key):
    # Takes a 3-letter key (e.g. "DBX") and converts it
    # to a numerical offset code. Alternatively, takes
    # a numerical offset code and converts it to a key.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if type(key) == str:
        num1 = alphabet.index(key[0]) + 1
        num2 = alphabet.index(key[1]) + 1
        num3 = alphabet.index(key[2]) + 1
        output = num1 * num2 * num3 - 1
        return output
    elif type(key) == int:
        key1 = key
        return key1

rotor1 = "JWEHLFUSDIBCPKNRMQTGOVZXAY"
rotor2 = "NGRTZJVYEQBSHPKLXDUAFCWMIO"
rotor3 = "NMLBWQGDIRPFUTJCXHSEKYOVAZ"
rotor4 = "LQCGTJAUEMWHZIPXDFSKYRNBVO"
rotor5 = "CMLIVZXANWPEDOBFRTGKJSUQYH"
reflector1 = "QYPJGWMRKLXHDECZVNUOFABTIS"

"""
This is the code for the inner components of the
ENIGMA machine.
"""

def useRotor(letter, direction, device, position):
    # This function changes the letter that's input
    # in the provided direction, using the specified
    # device (i.e. rotor, reflector, plugboard).
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    setting = alphabet.index(position)
    if direction == "in":
        letterNum = alphabet.index(letter)
        cipherletter = device[(setting + letterNum) % 26]
        return cipherletter
    elif direction == "out":
        letterNum = device.index(letter)
        cipherletter = alphabet[(letterNum - setting) % 26]
        return cipherletter

def moveRotors(offset):
    # This function simulates the movement of the
    # rotors by incrementing the current setting by 1.
    # It takes a key and outputs the incremented key.
    # e.g. input: ADG; output: ADH
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num1 = alphabet.index(offset[0])
    num2 = alphabet.index(offset[1])
    num3 = alphabet.index(offset[2])
    if offset[2] == "Z":
        if offset[1] == "Z":
            if offset[0] == "Z":
                num1 = 0
                num2 = 0
                num3 = 0
            else:
                num1 += 1
                num2 = 0
                num3 = 0
        else:
            num2 += 1
            num3 = 0
    else:
        num3 += 1
    k1 = alphabet[num1]
    k2 = alphabet[num2]
    k3 = alphabet[num3]
    newOffset = k1 + k2 + k3
    return newOffset

def useReflector(letter, device):
    # This function simulates the ENIGMA reflector.
    # The alphabet string is divided into pairs of letters.
    # If one member of a pair is input, the other is output.
    letterNum = device.index(letter)
    if letterNum % 2 == 0:
        return device[letterNum + 1]
    else:
        return device[letterNum - 1]
    
def usePlugboard(letter, plugboard):
    # This function simulates the ENIGMA plugboard.
    # 10 pairs of letters are made from a scrambled alphabet
    # string. If one member of a pair is input, the other is
    # output.
    if letter in plugboard:
        letterNum = plugboard.index(letter)
    else:
        return letter
    if letterNum % 2 == 0:
        return plugboard[letterNum + 1]
    else:
        return plugboard[letterNum - 1]
    
"""
This is the code that simulates the machine itself.
"""

def enigmaCharacter(letter, offset, daykey):
    # This function encodes a single character using the
    # current rotor positions.
    ime = usePlugboard(letter, daykey[2])
    ime = useRotor(ime, "in", daykey[1][2], offset[2])
    ime = useRotor(ime, "in", daykey[1][1], offset[1])
    ime = useRotor(ime, "in", daykey[1][0], offset[0])
    ime = useReflector(ime, reflector1)
    ime = useRotor(ime, "out", daykey[1][0], offset[0])
    ime = useRotor(ime, "out", daykey[1][1], offset[1])
    ime = useRotor(ime, "out", daykey[1][2], offset[2])
    ime = usePlugboard(ime, daykey[2])
    return ime
    
def enigma(message, messagekey, daykey):
    # This applies the Enigma encoding/decoding to
    # your message. The message must be a string of
    # capital letters with no spaces.
    output = ""
    offset = messagekey
    for char in message:
        enciphered = enigmaCharacter(char, offset, daykey)
        output += enciphered
        offset = moveRotors(offset)
    return output
