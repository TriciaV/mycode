#!/usr/bin/env python3
# if Check hostname against expected value

## accept input from user
hostname = input("Provide value for hostname?")

## use the lower method to test if input value matches expected value
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")
else:
    print("hostname does not match expected config")

## Always print out to the user
print("Exiting the script")

