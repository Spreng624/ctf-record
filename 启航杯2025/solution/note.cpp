#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define _BYTE unsigned char

void decrypt_flag(char *src, char *trg)
{
	unsigned char v6[] = {0x42, 0x37, 0xA1, 0x7C};
	int length = strlen(src);
	int i;

	for (i = 0; i < length; i++)
	{
		trg[i] = v6[i % 4] ^ src[i];
		trg[i] ^= i + 1;
	}
	trg[i] = 0;
}

int main()
{
	char Decrypted_flag[64];
	char flag[100] = "\x12\x7D\xE1\x2C\x01\x4A\xC4\x45\x78\x5E\xC9\x46\x78\x5D\x83\x0F\x37\x12\xD0\x45\x63\x42\xD5\x57\x76\x14\xDE\x06\x6E\x04\x8F\x3E\x50\x21\xE1\x3B\x53\x72\xB7\x6C\x5D\x79\xF7\x00";

	decrypt_flag(flag, Decrypted_flag);
	printf("Decrypted flag: %s\n", Decrypted_flag);
	return 0;
}