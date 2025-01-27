#include <stdio.h>
#include <stdint.h>

void tea(unsigned int *a1, int *a2)
{
    int result;      // eax
    int i;           // [esp+D0h] [ebp-38h]
    int v4;          // [esp+DCh] [ebp-2Ch]
    unsigned int v5; // [esp+F4h] [ebp-14h]
    unsigned int v6; // [esp+100h] [ebp-8h]

    v6 = *a1;
    v5 = a1[1];
    v4 = 0;
    for (i = 0; i < 32; ++i)
    {
        v4 -= 1640531527;
        v6 += (v4 + v5) ^ (a2[1] + (v5 >> 5)) ^ (*a2 + 16 * v5);
        v5 += (v4 + v6) ^ (a2[3] + (v6 >> 5)) ^ (a2[2] + 16 * v6);
    }
    *a1 = v6;
    a1[1] = v5;
}

int tea_de(uint32_t *a1, int a2)
{
    uint32_t v4;
    uint32_t v5;
    uint32_t v6;

    v6 = *a1;
    v5 = a1[1];
    v4 = -1914802624;
    for (int i = 0; i < 64; ++i)
    {
        v5 -= (*(unsigned int *)(a2 + 4 * ((v4 >> 11) & 3)) + v4) ^ (v6 + ((v6 >> 5) ^ (16 * v6)));
        v4 += 1640531527;
        v6 -= (*(unsigned int *)(a2 + 4 * (v4 & 3)) + v4) ^ (v5 + ((v5 >> 5) ^ (16 * v5)));
    }
    a1[0] = v6;
    a1[1] = v5;
    return 4;
}

int main()
{
    char v1;
    char v2;
    int i;
    unsigned char key1[] = {
        0x45, 0x12, 0x00, 0x00, 0x98, 0x32, 0x00, 0x00,
        0x56, 0x47, 0x00, 0x00, 0x63, 0x14, 0x00, 0x00};
    unsigned char key2[] = {
        0x12, 0x45, 0x00, 0x00, 0x32, 0x98, 0x00, 0x00,
        0x47, 0x56, 0x00, 0x00, 0x14, 0x63, 0x00, 0x00};
    unsigned char data[] = {
        0x60, 0xC3, 0x8D, 0x01, 0x57, 0x54, 0x83, 0xD5,
        0xCB, 0x2D, 0xEE, 0x8B, 0xEE, 0x2D, 0xBB, 0x92,
        0x54, 0xAD, 0xF4, 0xFD, 0x2D, 0x8C, 0x3F, 0x04,
        0xA9, 0x32, 0xA2, 0x61, 0xD1, 0xF4, 0x15, 0x0F,
        0x79, 0x49, 0xEA, 0x16, 0xDA, 0xF6, 0x2B, 0x7C,
        0x32, 0xFA, 0xD5, 0xDC, 0x19, 0x08, 0x45, 0x76};

    unsigned int *k = (unsigned int *)key1;
    // 处理密钥
    for (i = 0; i < 4; ++i)
    {
        *(k + i) ^= 0xABCDu;
    }

    for (i = 0; i < 6; ++i)
    {
        tea(data + 8 * i, key1);
    }

    for (i = 0; i < 6; ++i)
        tea_de(data + 8 * i, key2);

    printf("%44s\n", data); // 0xGame{a7961e4b-c809-f340-412e-91abd2c9b535}

    return 0;
}