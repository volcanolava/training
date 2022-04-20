#include <stdio.h>

extern unsigned long _my_add(long, long);
extern unsigned long _my_mul(long, long);

int main(void) {
    /*printf("cf 1: %lu\n", _my_add(0xFFFFFFFFFFFFFFFF, 1)); //cf exampke 
    printf("of 1: %lu\n", _my_add(0xEFFFFFFFFFFFFFFF, 1)); //of example
    printf("zf 1: %lu\n", _my_add(0, 0)); //zf example
    printf("pf 0: %lu\n", _my_add(0, 1)); //pf 0 example
    printf("pf 1: %lu\n", _my_add(1, 1)); //pf 1 example
    printf("sf 1: %lu\n", _my_add(0xFFFFFFFFFFFFFFFF, 0)); //sf 1 example
    printf("sf 0: %lu\n", _my_add(0x7FFFFFFFFFFFFFFF, 0)); //sf 0 example
    printf("af 1: %lu\n", _my_add(0x1000, 1)); //af 1 example
    printf("af 0: %lu\n", _my_add(0x0100, 1)); //af 0 example*/
    printf("reg: %lu\n", _my_add(6000, 545)); //regular addition

    printf("reg: %lu\n", _my_mul(20, 5)); //regular multiplication, cf=of=0
    printf("reg: %lu\n", _my_mul(0x128765, 0x10000)); //regular multiplication, cf=of=1
    return 0;
}