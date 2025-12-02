package main

import (
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/lestrrat-go/jwx/v2"
)

func main() {
	// Print the example GitHub PAT secret part 2
	fmt.Println("GitHub secret token:", "ghp_A1bC2dE3fH4iJ5kL6mN7oP8qR9sT0uVwXyZ1F")
	_ = jwx.GuessFormat([]byte("{}"))
	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("welcome"))
	})
	http.ListenAndServe(":3000", r)
}
