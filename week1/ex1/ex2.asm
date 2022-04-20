global _my_add
global _my_mul

section .data
CARRYF_MASK EQU 0x01
PARITYF_MASK EQU 0x04
AUXF_MASK EQU 0x10
ZEROF_MASK EQU 0x40
SIGNF_MASK EQU 0x80
OVERFLOWF_MASK EQU 0x800

MAX_UINT EQU 0xFFFFFFFFFFFFFFFF
AUX_MASK EQU 0x0001000100010000
SIGN_MASK EQU 0x8000000000000000

FLAGS_TO_ZERO EQU 0xFFFFFFFFFFFFF72A
MUL_FLAGS_TO_ZERO EQU 0xFFFFFFFFFFFFF7FE

section .bss

section .text

_my_add:
    push rbp
    mov rbp, rsp 

    push rbx 
    push rcx 
    push rdx
    push r9
    push r10
    push r11

    xor rcx, rcx ;carry counter
    xor r8, r8 ;and mask

    ;original sign
    xor r9, r9
    test rdi, 0x8000000000000000
    jz new_sign_holder
    mov r9, 1

    new_sign_holder:
    ; new sign holder
    xor r10, r10
    next:
    mov rbx, rdi ;carry
    and rbx, rsi
    shl rbx, 1

    or r8, rbx; update and mask

    xor rdi, rsi ;addition
    mov rsi, rbx ; mov carry for next iteration

    inc rcx

    cmp rsi, 0
    jnz next

    mov rax, rdi ;result

    ;flags 
    pushfq
    pop rdx

    and rdx, FLAGS_TO_ZERO

    checkzf:
    cmp rax, 0
    jnz checkpf
    setzf:
    or rdx, ZEROF_MASK
    checkpf:
    test rax, 1
    jnz checksf
    setpf:
    or rdx, PARITYF_MASK
    checksf:
    mov r11, 0x8000000000000000
    test rax, r11
    jz checkcf
    setsf:
    or rdx, SIGNF_MASK
    mov r10, 1
    checkcf:
    cmp rcx, 64d
    jnz checkof
    cmp rax, 0
    jnz checkof
    setcf:
    or rdx, CARRYF_MASK
    checkof:
    xor r9, r10
    jz checkaf
    setof:
    or rdx, OVERFLOWF_MASK
    checkaf:
    test r8, AUX_MASK
    jz set_flags
    setaf:
    or rdx, AUXF_MASK
    set_flags:
    push rdx
    popfq

    pop r11
    pop r10
    pop r9
    pop rdx
    pop rcx
    pop rbx

    mov rsp, rbp
    pop rbp
    ret

_my_mul:
    push rbp
    mov rbp, rsp

    push rbx 
    push rcx
    push rdx
    push r9

    mov rax, rdi
    mov rbx, rdi

    mov rcx, rsi
    dec rcx
    _add_once:
    mov rdi, rax
    mov rsi, rbx
    call _my_add
    loop _add_once

    
    ;flags
    pushfq
    pop rdx
    mov r9, MUL_FLAGS_TO_ZERO
    and rdx, r9

    mov r9, 0xffffffff00000000
    test rax, r9
    jz _set_flags
    or rdx, OVERFLOWF_MASK
    or rdx, CARRYF_MASK

    _set_flags:
    push rdx
    popfq

    pop r9
    pop rdx
    pop rcx
    pop rbx

    mov rsp, rbp
    pop rbp
    ret