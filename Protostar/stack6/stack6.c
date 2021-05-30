#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void getpath()
{
  char buffer[64];
  unsigned int ret;

  printf("input path please: "); fflush(stdout);

  gets(buffer);

  ret = __builtin_return_address(0); //this function checks the current return address in memory

  if((ret & 0xbf000000) == 0xbf000000) { // here we perform the AND operation and check if the result starts with 0xbf
      printf("bzzzt (%p)\n", ret); //if the return address starts with 0xbf print the return address and exit   
      _exit(1);
  }

  printf("got path %s\n", buffer);
}

int main(int argc, char **argv)
{
  getpath();
}