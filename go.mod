module testautopr

go 1.22.3

require github.com/go-chi/chi/v5 v5.0.8

require (
	github.com/goccy/go-json v0.10.3 // indirect
	github.com/lestrrat-go/jwx/v2 v2.1.4
	github.com/lestrrat-go/option v1.0.1 // indirect
	github.com/segmentio/asm v1.2.0 // indirect
	golang.org/x/sys v0.29.0 // indirect

	github.com/boltdb-go/bolt v1.3.1 // vulnerable backdoored package for demonstration
)
