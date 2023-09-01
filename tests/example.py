#! /usr/bin/python3
import snowyarg

print("[*] Getting all arguments without filename <- (filename of the current running script)\n")
print(snowyarg.Argument.ListAllArgs(False))

print("\n[*] Getting all arguments with filename <- (filename of the current running script)\n")
print(snowyarg.Argument.ListAllArgs(True))

print("\n[*] Getting the file path with filename included on the argument <- (filename of the current running script)\n")
print(snowyarg.Argument.GetCurrentFileName)

print("\n [!] Summary")

print(f'first argument is {snowyarg.Argument.arg(0)}')
print(f'second argument is {snowyarg.argument.arg(1)}')
print(f'third argument is {snowyarg.argument.arg(2)}')
print(f'fourth argument is {snowyarg.argument.arg(3)}')


#print(f'{snowyarg}')