#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 加密函数
char *crypt(const char *Game_key)
{
    unsigned char Key[] = "This is: True_KEY!for #0xgAmE_Unity~Cryption";
    int num = 0;
    // unsigned char array[] = "E!>\u0008W1\tMBEBD]ZKKRV\u0016DfEl@WD35Qu\rX\u0015q\u0011\u001B\u000B\u0008v\u0004O\\h<";
    unsigned char array[] = "E!>\x08W1\tMBEBD]ZKKRV\026DfEl@WD35Qu\rX\x15q\x11\x1B\x0B\x08v\x04O\\h<";
    for (int i = 0; i < 44; i++)
    {
        num = (num + (int)Game_key[i % strlen(Game_key)]) % 44;
        unsigned char b = Key[num];
        Key[num] = Key[i];
        Key[i] = b;
    }

    for (int j = 43; j >= 0; j--)
    {
        array[j] ^= Key[j];
    }

    // 将加密后的数组转换为字符串并返回
    char *encrypted = (char *)malloc(45); // 分配足够的内存来存储加密后的数据和空字符
    memcpy(encrypted, array, 44);
    encrypted[44] = '\0'; // 确保字符串以空字符结尾
    return encrypted;
}

int main()
{
    char *enc_data = crypt("0xoX0XOxOXoxGAME");
    printf("%s\n", enc_data); // 0xGame{36ecd059-b3e7-73c8-fa80-0a2abef3c757}
    free(enc_data);           // 释放分配的内存
    return 0;
}