```
sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'
gcc overflow.c -o overflow -fno-stack-protector -z execstack -no-pie

```

# STACK 0

* All we need to do is overwrite the buffer variable into the modified variable


# STACK 1

* We need to overflow the buffer and then overwrite the variable

```
python -c 'print "A"*64 + "\x64\x63\x62\x61" '
```

# STACK 3

* Here we are working with environment variables. Since the variable gets loaded into a buffer, we can use the env variable to overflow the buffer and change the value of the variable

# STACK 4

* Here our goal is to gain control of the eip and point it to the address of another function
* The EIP is not necessarily immediately after the buffer so we need to determine the padding that gets us to where EIP is

# STACK 5

* This was rather interesting. A classic stack based BOF where we inject shellcode to get us a shell
* When debugging with GDB, addresses slightly get shifted upwards, Which was the case here
* We need to compensate for this using a NOP sled and adjust the return address to hit the NOP sled in the stack

# STACK 6

* This challenge involved bypassing stack pointer restrictions.
* The program we are given prevents us from executing code on the stack by exiting once the return address is pointing to the stack

## STACK BYPASS TECHNIQUES

* A ret2libc (return to libc, or return to the C library) attack is one in which the attacker does not require any shellcode to take control of a target, vulnerable process.
