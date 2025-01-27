#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <windows.h>
#include <wincrypt.h>
#include <time.h>
#include <stdarg.h>

#define _BYTE unsigned char
#define _DWORD unsigned long
#define _WORD unsigned short
#define LOBYTE(x) (*((_BYTE *)&(x)))
#define LODWORD(x) (*((_DWORD *)&(x)))
#define SHIDWORD(x) (((__int32)&(x) + 1))

int func_65(__int64 a1, unsigned __int8 a2)
{
    if (a2 >= 0x40u)
    {
        LODWORD(a1) = SHIDWORD(a1) >> 31;
    }
    else if (a2 >= 0x20u)
    {
        LODWORD(a1) = SHIDWORD(a1) >> (a2 & 0x1F);
    }
    else
    {
        a1 >>= a2 & 0x1F;
    }
    return a1;
}

void func_41(unsigned char *pbData, uint32_t dwDataLen)
{
    int v3;                 // edx
    uint32_t i;             // [esp+D0h] [ebp-78h]
    char v7[72];            // [esp+DCh] [ebp-6Ch] BYREF
    uint32_t pdwDataLen[3]; // [esp+124h] [ebp-24h] BYREF
    int phProv[3];          // [esp+130h] [ebp-18h] BYREF
    int phHash[2];          // [esp+13Ch] [ebp-Ch] BYREF
    int savedregs;          // [esp+148h] [ebp+0h] BYREF

    phProv[0] = 0;
    pdwDataLen[0] = 4;
    printf("pbData: %s, dwDataLen: %d\n", pbData, dwDataLen);
    CryptAcquireContextW((HCRYPTPROV *)phProv, 0, 0, 1u, 0);
    CryptCreateHash(phProv[0], 0x8004u, 0, 0, (HCRYPTHASH *)phHash);
    CryptHashData(phHash[0], pbData, dwDataLen, 0);
    CryptGetHashParam(phHash[0], 2u, 0, pdwDataLen, 0);
    CryptGetHashParam(phHash[0], 2u, (unsigned char *)v7, pdwDataLen, 0);
    printf("0xGame{");
    for (i = 0; i < 20; ++i)
        printf("%02x", v7[i] & 0xFFu);
    printf("}\n");

    CryptDestroyHash(phHash[0]);
    CryptReleaseContext(phProv[0], 0);
}

int main()
{
    int v3;        // ecx
    int v4;        // edx
    int v5;        // edx
    __int64 v7;    // [esp-8h] [ebp-190h]
    int i;         // [esp+D0h] [ebp-B8h]
    char v8;       // [esp+DFh] [ebp-A9h]
    time_t v9;     // [esp+E8h] [ebp-A0h]
    char Text[72]; // [esp+F8h] [ebp-90h] BYREF
    char Buf2[68]; // [esp+140h] [ebp-48h] BYREF
    int savedregs; // [esp+188h] [ebp+0h] BYREF

    char Str[10] = "0xGameUser";

    v9 = time(0);
    LOBYTE(v3) = 28;
    v8 = func_65(v3, SHIDWORD(v9));
    // v8 = 0x3;
    printf("v8: %d\n", v8);

    for (i = 0; i < 10; ++i)
    {
        Str[i] ^= v8;
        printf("%c", Str[i]);
    }
    printf("\n");
    func_41((unsigned char *)Str, 0xAu);
    // 0xGame{cbb6c62bc5b4a113c7fdfd1e85425ea50bd0729a}

    return 0;
}