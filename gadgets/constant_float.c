#include <stdio.h>

double input[9] = {	 2.8628345837198785e-312,
	-6.7936696184209404e-229,
	-6.7936699762396021e-229,
	3.0226914823032513e+274,
	-2.6710638803933159e-229,
	-2.6710638803930354e-229,
	2.9212589871283409e+274,
	-6.8283971717601484e-229,
	-6.9693174593711226e-229};

int main()
{
	for(int i = 0; i < 9; ++i)
	{
		printf("0x%lx\n", *(unsigned long*)&input[i]);
	}
}
