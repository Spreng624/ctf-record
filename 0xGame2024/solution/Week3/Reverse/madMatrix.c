#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

// hello: 复制a1到a2
// a1: 矩阵数值 4*9
// a2：4+4+4*9=44, 行+列+数据
unsigned __int8 *hello(__int64 a1, unsigned __int8 *a2)
{
    for (int i = 0; i < 9; ++i)
    {
        *(uint32_t *)(*((uint64_t *)a2 + 1) + 4 * i) = *(uint32_t *)(a1 + 4 * i);
    }
    return a2;
}

// 生成矩阵input->memory
// memory: 存储
// input: 输入的44位字符串
void Morpheus(__int64 memory, __int64 input)
{
    __int64 v5;        // [rsp+0h] [rbp-80h]
    __int32 v6[64];    // 4 * 64
    unsigned char *v7; // [rsp+120h] [rbp+A0h]
    int j;             // [rsp+128h] [rbp+A8h]
    int i;             // [rsp+12Ch] [rbp+ACh]

    memset(&v5 + 4, 0, 0x100u); // 初始化v5

    // 将input的内容复制到v6
    // 44*1->44*4=176 用0填充
    for (i = 0; *(unsigned char *)(input + i); ++i)
        v6[i] = *(char *)(input + i);

    for (j = 0; j < 7; ++j)
    {
        // 清空v7
        v7 = malloc(0x10u);
        *v7 = 3;
        v7[1] = 3;
        *((int64_t *)v7 + 1) = malloc(0x24u);

        // 44*4 -> 7* 4*6
        if (&v6[6 * j])
            // v7 = 4+4+ 36 = 32
            //
            hello((__int64)&v6[6 * j], v7);
        // memery = 7* 8*8= 448
        *(int64_t *)(memory + 8 * j) = v7;
    }
}
// 计算行列式值
__int64 Neo(unsigned __int8 *a1)
{
    FILE *v1;          // rax
    __int64 result;    // rax
    FILE *v3;          // rax
    int v4;            // ebx
    void *Memory;      // [rsp+28h] [rbp-58h]
    uint32_t *v6;      // [rsp+30h] [rbp-50h]
    unsigned __int8 y; // [rsp+38h] [rbp-48h]
    unsigned __int8 x; // [rsp+39h] [rbp-47h]
    unsigned __int8 i; // [rsp+3Ah] [rbp-46h]
    char v10;          // [rsp+3Bh] [rbp-45h]
    unsigned int v11;  // [rsp+3Ch] [rbp-44h]
    char *v12;         // [rsp+60h] [rbp-20h]

    v12 = (char *)a1;
    x = a1[0];
    y = a1[1];

    if (x != y)
    {
        v1 = (FILE *)__acrt_iob_func(2);
        fwrite("ERROR:Det Matrix input is not sqare matrix!", 1u, 0x2Bu, v1);
        return 0;
    }

    v6 = (uint32_t *)*((uint64_t *)a1 + 1);
    // 行列式阶数
    switch (x)
    {
    case 0:
        v3 = (FILE *)__acrt_iob_func(2);
        fwrite("ERROR:Det Matrix input is zero!", 1u, 0x1Fu, v3);
        return 0;
    case 1:

        return **((unsigned int **)a1 + 1);

    case 2:
        return (unsigned int)(v6[3] * *v6 - v6[1] * v6[2]);

    default:
        v11 = 0;
        v10 = 1;
        Memory = malloc(0x10u);
        *(unsigned char *)Memory = x - 1;
        *((unsigned char *)Memory + 1) = y - 1;
        *((uint64_t *)Memory + 1) = malloc(4 * (x - 1) * (__int64)(y - 1));
        for (i = 0; i < x; ++i)
        {
            leftMatrix(0, i, v12, Memory);
            v4 = v6[i] * v10;
            v11 += v4 * (unsigned __int64)Neo(Memory);
            v10 = -v10;
        }
        free(*((void **)Memory + 1));
        free(Memory);
        return v11;
    }
}
// 乘法 a1*a2->a3
__int64 guess(unsigned __int8 *a1, __int64 a2, __int64 a3)
{
    unsigned __int8 v4; // [rsp+Eh] [rbp-12h]
    unsigned __int8 v5; // [rsp+Fh] [rbp-11h]
    unsigned __int8 v6; // [rsp+10h] [rbp-10h]
    unsigned __int8 k;  // [rsp+11h] [rbp-Fh]
    unsigned __int8 j;  // [rsp+12h] [rbp-Eh]
    unsigned __int8 i;  // [rsp+13h] [rbp-Dh]
    int v10;            // [rsp+14h] [rbp-Ch]
    int v11;            // [rsp+18h] [rbp-8h]
    int v12;            // [rsp+1Ch] [rbp-4h]

    // a3 有前缀
    if (!a3)
        return 0;
    if ((unsigned __int8 *)a3 == a1 || a3 == a2)
        return 0;
    // a1行数=a2列数
    if (a1[1] != *(unsigned char *)a2)
        return 0;
    v12 = 0;
    v11 = 0;
    v6 = *a1;
    v5 = a1[1];
    v4 = *(unsigned char *)(a2 + 1);
    // 穷举所有可能的乘法
    for (i = 0; i < a1[0]; ++i)
    {
        for (j = 0; j < v4; ++j)
        {
            //a3[v12] = a1[i] * a2[j]
            *(uint32_t *)(*(uint64_t *)(a3 + 8) + 4 * v12) = 0;
            v10 = 0;
            for (k = 0; k < v5; ++k)
            {
                *(uint32_t *)(*(uint64_t *)(a3 + 8) + 4 * v12) +=
                    *(uint32_t *)(*(uint64_t *)(a2 + 8) + 4 * (v10 + j)) *
                    *(uint32_t *)(*((uint64_t *)a1 + 1) + 4 * (v11 + k));
                v10 += v4;
            }
            ++v12;
        }
        v11 += v5;
    }
    return a3;
}
// 比较矩阵
int byebye(unsigned __int8 *a1, const void *a2)
{
    int result; // eax

    if (*a1 * a1[1] == 9)
        result = memcmp(*((const void **)a1 + 1), a2, 36);
    else
        result = -1;
    return result;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
    char v4;  // [rsp+20h] [rbp-60h]
    char v5;  // [rsp+50h] [rbp-30h]
    char v6;  // [rsp+51h] [rbp-2Fh]
    char *v7; // [rsp+58h] [rbp-28h]

    char v8;   // [rsp+60h] [rbp-20h]
    char v9;   // [rsp+90h] [rbp+10h]
    char v10;  // [rsp+91h] [rbp+11h]
    char *v11; // [rsp+98h] [rbp+18h]

    char v12;  // [rsp+A0h] [rbp+20h]
    char v13;  // [rsp+D0h] [rbp+50h]
    char v14;  // [rsp+D1h] [rbp+51h]
    char *v15; // [rsp+D8h] [rbp+58h]

    char v16;  // [rsp+E0h] [rbp+60h]
    char v17;  // [rsp+110h] [rbp+90h]
    char v18;  // [rsp+111h] [rbp+91h]
    char *v19; // [rsp+118h] [rbp+98h]

    char *v20; // [rsp+120h] [rbp+A0h]
    char *v21; // [rsp+128h] [rbp+A8h]
    char *v22; // [rsp+130h] [rbp+B0h]
    char *v23; // [rsp+138h] [rbp+B8h]

    char Str;            // [rsp+2C0h] [rbp+240h]
    unsigned char *v28;  // [rsp+300h] [rbp+280h]
    unsigned int lenStr; // [rsp+308h] [rbp+288h]
    int j;               // [rsp+310h] [rbp+290h]
    int k;               // [rsp+314h] [rbp+294h]
    int i;               // [rsp+318h] [rbp+298h]
    int v33;             // [rsp+31Ch] [rbp+29Ch]

    printf("Welcome to the test of Mad Matrix.\nNow you are allowed to input flag:");
    memset(&Str, 0, 0x240u);
    scanf("%64s", &Str);
    lenStr = strlen(&Str);

    // KeyMatrix_Array 1000 3000 1000 0000 2000 1000 1000 2000 0000
    // unk_404044      1000 2000 2000 3000 5000 6000 0000 2000 1000
    // unk_404068      0000 4000 3000 1000 2000 1000 2000 3000 1000
    // unk_40408C      1000 2000 3000 3000 5000 6000 1000 4000 A000
    // unk_4040C0     E8100C0100 2000 3000 4000 5000 2000 3000 4000
    char *unk_404044 = {1, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0};
    char *unk_40408C = {1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0xA, 0, 0, 0};
    char *KeyMatrix_Array = {1, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0};
    char *unk_404068 = {0, 0, 0, 0, 4, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0};

    unsigned char unk_4040C0[] = {
        0xE8, 0x1, 0x0, 0x0, 0xC0, 0x1, 0x0, 0x0,
        0x81, 0x1, 0x0, 0x0, 0x57, 0x5, 0x0, 0x0,
        0xD3, 0x4, 0x0, 0x0, 0x1E, 0x4, 0x0, 0x0,
        0x3D, 0x1, 0x0, 0x0, 0x11, 0x1, 0x0, 0x0,
        0x2, 0x1, 0x0, 0x0, 0x6C, 0x2, 0x0, 0x0,
        0x40, 0x1, 0x0, 0x0, 0x45, 0x1, 0x0, 0x0,
        0xB7, 0x5, 0x0, 0x0, 0xEC, 0x2, 0x0, 0x0,
        0xF3, 0x2, 0x0, 0x0, 0xE9, 0x5, 0x0, 0x0,
        0x1D, 0x3, 0x0, 0x0, 0x36, 0x3, 0x0, 0x0,
        0x4D, 0x1, 0x0, 0x0, 0x0A, 0x1, 0x0, 0x0,
        0x92, 0x1, 0x0, 0x0, 0xD, 0x0, 0x0, 0x0,
        0x9F, 0x0, 0x0, 0x0, 0xF5, 0x0, 0x0, 0x0,
        0xBD, 0x0, 0x0, 0x0, 0xA1, 0x0, 0x0, 0x0,
        0x1, 0x1, 0x0, 0x0, 0x62, 0x1, 0x0, 0x0,
        0x47, 0x1, 0x0, 0x0, 0x23, 0x2, 0x0, 0x0,
        0xFB, 0x0, 0x0, 0x0, 0xC0, 0x0, 0x0, 0x0,
        0x26, 0x1, 0x0, 0x0, 0x91, 0x1, 0x0, 0x0,
        0x23, 0x1, 0x0, 0x0, 0xB7, 0x1, 0x0, 0x0,
        0xF0, 0x0, 0x0, 0x0, 0xFD, 0x0, 0x0, 0x0,
        0x0D, 0x1, 0x0, 0x0, 0x9E, 0x2, 0x0, 0x0,
        0xC0, 0x2, 0x0, 0x0, 0xF1, 0x2, 0x0, 0x0,
        0x91, 0x0, 0x0, 0x0, 0x9F, 0x0, 0x0, 0x0,
        0xA4, 0x0, 0x0, 0x0, 0x29, 0x2, 0x0, 0x0,
        0x3B, 0x1, 0x0, 0x0, 0x2E, 0x1, 0x0, 0x0,
        0xE4, 0x4, 0x0, 0x0, 0xD8, 0x2, 0x0, 0x0,
        0xC7, 0x2, 0x0, 0x0, 0xBD, 0x5, 0x0, 0x0,
        0x25, 0x3, 0x0, 0x0, 0xE4, 0x2, 0x0, 0x0,
        0xC7, 0x1, 0x0, 0x0, 0x51, 0x1, 0x0, 0x0,
        0xD5, 0x0, 0x0, 0x0, 0xFE, 0x0, 0x0, 0x0,
        0xE5, 0x0, 0x0, 0x0, 0x6E, 0x0, 0x0, 0x0,
        0x2C, 0x1, 0x0, 0x0, 0xA0, 0x0, 0x0, 0x0,
        0x9E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0};

    v20 = 0;
    v13 = 3;
    v14 = 3;
    v15 = &v12;
    hello((__int64)&unk_404044, (unsigned __int8 *)&v13); // 9
    v20 = &v13;

    v21 = 0;
    v5 = 3;
    v6 = 3;
    v7 = &v4;
    hello((__int64)&unk_40408C, (unsigned __int8 *)&v5); // 9
    v21 = &v5;

    v22 = 0;
    v17 = 3;
    v18 = 3;
    v19 = &v16;
    hello((__int64)&KeyMatrix_Array, (unsigned __int8 *)&v17); // 9
    v22 = &v17;

    v23 = 0;
    v9 = 3;
    v10 = 3;
    v11 = &v8;
    hello((__int64)&unk_404068, (unsigned __int8 *)&v9); // 9
    v23 = &v9;

    // v29

    void *v24[8]; // 中间变量矩阵

    // 初始化v24，加前缀
    memset(v24, 0, sizeof(v24));
    for (i = 0; i < 7; ++i)
    {
        v28 = malloc(0x10u);
        *v28 = 3;
        v28[1] = 3;
        *((uint64_t *)v28 + 1) = malloc(0x24u);
        v24[i] = v28;
    }

    void *Memory[8];        // 指向44位flag生成的7个矩阵，有前缀
    Morpheus(Memory, &Str); // str长度44

    // Dst: 操作结果7个矩阵
    // Memory: 指向44位flag生成的7个矩阵
    // v20: 辅助的4个矩阵
    // v24: 中间变量矩阵7个矩阵

    // 7矩阵格式：36Byte一个矩阵，252Byte,无前缀

    char Dst[256];
    memcpy(Dst, &unk_4040C0, 0xFCu);

    for (int i = 0; i < 7; i++)
    {
        // 如果v20的行列式的值不为0, 则进行乘法运算, v24暂存中间结果
        if ((unsigned int)Neo((&v20)[i % 4]))
            guess((unsigned __int8 *)(&v20)[i % 4], (__int64)Memory[i], (__int64)v24[i]);

        if (byebye((unsigned __int8 *)v24[i], &Dst[36 * i]))
            printf("Wrong. Try again.\n");
        return 0;
    }

    printf("Correct! Your flag has passed the test.\n");
    return 0;
}