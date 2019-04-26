#include <stdio.h>
#include <stdlib.h>

int fun(int a)
{
    int b = a + 99;
    return b;
}

int main()
{
    char c[20] = {"flag{abcd_hello}"};
    int a = 0;
    printf("Try to kill me!\n");
    fun(a);
    a = fun(a);
    printf("Hello, world!\n");
    return 0;
}