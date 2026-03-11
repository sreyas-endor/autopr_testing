package main

import (
	"fmt"
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"github.com/lestrrat-go/jwx/v2"
)

func main() {
	// Print the example GitHub PAT secret
	fmt.Println("GitHub secret token:", "THISISSREYASPAT_IFYOUSEETHISMESSAGETHEPATISLEAKED") // pragma: allowlist secret
	// Dummy GCLOUD_API_KEY for scanner test
	fmt.Println("GCloud API key:", "THIS_IS_A_DUMMY_KEY") // pragma: allowlist secret

	_ = jwx.GuessFormat([]byte("{}"))
	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("welcome"))
	})
	http.ListenAndServe(":3000", r)
}
