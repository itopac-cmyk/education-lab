/**
 * YARA Rule: Detects a generic stack-based buffer overflow exploit 
 * targeting a specific function.
 */
rule Detect_VulnBufferOverflow_Exploit {
    meta:
        author = "Isa Topac - Education Lab"
        description = "Detects exploitation attempts on vuln_buffer_overflow.c"
        severity = "High"

    strings:
        // A long string of NOPs (\x90) often used as a 'NOP Sled'
        $nop_sled = { 90 90 90 90 90 90 90 90 }
        
        // Potential shellcode (placeholder)
        $shellcode_marker = { 31 c0 50 68 2f 2f 73 68 68 2f 62 69 6e 89 e3 50 53 89 e1 b0 0b cd 80 }

    condition:
        // Detect if a very long string (> 16 chars) is used as an argument
        // OR a common NOP sled / shellcode is found in memory
        $nop_sled or $shellcode_marker
}
