## SHELLCODING FOR HACKERS

# Chapter 1: introduction to exploitation: linux on x86


**Memory management**

* When a program is executed, it is laid out in an organized manner- various elements of the program are mapped into memory. 
* First the OS creates an address space in which the program will run
* This address space includes the actual program instructions as well as any required data.
* Next information is loaded from the program's executable file to the newly created address space. There are 3 types of segments: .text, .bss and .data
* The .text segment is mapped as read-only, .data and .bss are writable and are reserved for global variables.
* .data has static initialized data, and the .bss segment contains uninitialized data.
* .text holds program instructions
* Finally the stack and the heap are initialized	

**Registers**

* From a high level, registers can be grouped into four categories

1. General purpose - performas a range of common mathematical operations. They include registers such as eax, ebx, exc for the ia32, and can be used to store data and addresses, offset addresses, perform counting functions, and many other things. esp is a special register that points to the memory address where the next stack operation will take place. 
2. Segment - unlike other registers on a ia32 processor, the segment registers are 16 bit. others are 32 bit. These are like cs, ds, ss which are used to keep track of segments and to allow backword compatibility with 16 bit applications
3. Control - controls the function of the processor. The most important is the EIP that contains the address of the next machine intstruction to be executed. 
4. Other