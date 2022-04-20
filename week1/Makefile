CC := gcc
AS := nasm
LD := ld
MAKE := make

CFLAGS = -Wall -Werror
CFLAGS_32 = -m32
CFLAGS_64 = -m64
NOLINK = -c

ASFLAGS =
ASFLAGS_32 = -f elf32
ASFLAGS_64 = -f elf64
ASNAKED = -f bin

FINAL_TARGETS = ex1 ex2
TEMP_TARGETS = ex1_asm.o ex1_x32.o ex2_asm.o ex2_x64.o

.PHONY: all
all: $(FINAL_TARGETS)

ex2_asm.o: ex2.asm
	$(AS) $(ASFLAGS) $(ASFLAGS_64)  $< -o $@

ex2_x64.o: ex2.c
	$(CC) $(CFLAGS) $(CFLAGS_64) $(NOLINK) $< -o $@

ex2: ex2_x64.o ex2_asm.o
	$(CC) $(CFLAGS) $(CFLAGS_64) $^ -o $@

ex1_asm.o: ex1.asm
	$(AS) $(ASFLAGS) $(ASFLAGS_32)  $< -o $@

ex1_x32.o: ex1.c
	$(CC) $(CFLAGS) $(CFLAGS_32) $(NOLINK)  $< -o $@

ex1: ex1_asm.o ex1_x32.o
	$(CC) $(CFLAGS) $(CFLAGS_32) $^ -o $@

.PHONY: clean_temp
clean_temp:
	-rm -f $(TEMP_TARGETS)
	
.PHONY: clean
clean: clean_temp
	-rm -f $(FINAL_TARGETS)

