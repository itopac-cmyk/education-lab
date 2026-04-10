#include <stdio.h>
#include <string.h>

/**
 * VULNERABLE FUNCTION:
 * This function uses 'strcpy' on a fixed-size buffer without 
 * checking the input length. A classic entry point for zero-days.
 */
void process_input(char *user_input) {
    char buffer[16];
    
    // Copying input without bound checking
    printf("Processing: %s\n", user_input);
    strcpy(buffer, user_input);
    
    printf("Buffer contains: %s\n", buffer);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }

    process_input(argv[1]);
    printf("Program exited normally.\n");
    return 0;
}
