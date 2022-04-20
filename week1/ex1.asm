global _fibonacci

section .data

section .bss

section .text

_fibonacci:
    push ebp
    mov ebp, esp

    push ebx
    push ecx
    push edx

    xor ebx, ebx
    mov eax, 1

    mov ecx, [ebp + 8]
    cmp ecx, 1
    jb _ret_fib

    _loop_start:
    mov edx, eax
    add eax, ebx
    mov ebx, edx
    loop _loop_start

    _ret_fib:
    mov eax, ebx

    pop edx
    pop ecx
    pop ebx

    mov esp, ebp
    pop ebp
    ret 