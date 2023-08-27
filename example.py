#! /usr/bin/python3
import snowyarg

print("[*] Getting all arguments without filename <- (filename of the current running script)\n")
print(snowyarg.ListAllArgs(False))

print("\n[*] Getting all arguments with filename <- (filename of the current running script)\n")
print(snowyarg.ListAllArgs(True))

print("\n[*] Getting the file path with filename included on the argument <- (filename of the current running script)\n")
print(snowyarg.GetCurrentFileName())

print("\n [!] Summary")

arguments = snowyarg.ListAllArgs(False)
print(f'first argument is {arguments[0]}')
print(f'second argument is {arguments[1]}')
print(f'third argument is {arguments[2]}')
print(f'fourth argument is {arguments[3]}')