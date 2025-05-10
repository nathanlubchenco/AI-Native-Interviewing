package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/hello", helloHandler)
    http.ListenAndServe(":8080", nil)
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
    user := r.Context().Value("user")
    if user == nil {
        w.WriteHeader(http.StatusUnauthorized)
        return
    }
    fmt.Fprintf(w, "Hello, %v!", user)
}