#include <stdio.h>
#include <stdint.h>

void preProcess(char *a1, int len)
{
    char *i = &a1[len - 1];
    char v5;

    while (1)
    {
        if (a1 >= i)
            break;
        v5 = *a1;
        *a1 = *i;
        *i = v5;
        ++a1;
        --i;
    }
}

void tea_dec(uint32_t *data, uint32_t *k)
{
    uint32_t v3 = data[0];
    uint32_t v4 = data[1];
    int v5 = -1640531527 * 32;
    for (int i = 0; i < 32; ++i)
    {
        v4 -= (v3 + v5) ^ ((v3 >> 5) + k[3]) ^ (k[2] + 16 * v3);
        v3 -= (v4 + v5) ^ ((v4 >> 5) + k[1]) ^ (*k + 16 * v4);
        v5 += 1640531527;
    }
    data[0] = v3;
    data[1] = v4;
}

int main()
{
    char data[] = {
        0xC9, 0xB6, 0x5C, 0xCE, 0xF8, 0xEE, 0x8E, 0xA2, 0x33, 0x36,
        0x34, 0x63, 0x37, 0x32, 0x36, 0x64, 0x38, 0x37, 0x65, 0x33,
        0x62, 0x33, 0x63, 0x64, 0x36, 0x39, 0x64, 0x34, 0x64, 0x30,
        0x62, 0x38, 0x2A, 0x7A, 0x7C, 0x3B, 0x85, 0x33, 0x6D, 0xD3};

    char k[] = {
        0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x02, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00};

    preProcess(&data, 40);
    for (int i = 0; i < 5; i++)
    {
        tea_dec((uint32_t *)(__int64)&data[32 * i], (uint32_t *)(__int64)&k);
    }
    printf("%s\n", data); // 0xGame{e8b0d4d96dc3b3e78d627c463c9953a1}

    return 0;
}
