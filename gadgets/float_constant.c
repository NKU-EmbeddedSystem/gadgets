#include <stdio.h>

long input = 0;

int main(int argc, char **argv)
{
	scanf("%lx", &input);
	printf("intput : %lx, addr : 0x%lu \n", input, &input);
	void * addr = (void*)&input;
	printf("%lx\t%lf\n", *(long*)addr, *(double*)addr);
}
