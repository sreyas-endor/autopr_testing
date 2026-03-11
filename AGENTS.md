# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal single-file Go HTTP server (`main.go`) with no external service dependencies.

### Running the application

- `go run main.go` starts the server on **port 3000**.
- `GET /` returns `"welcome"`.

### Lint / Test / Build

- **Lint:** `go vet ./...`
- **Test:** `go test ./...` (no test files exist currently)
- **Build:** `go build -o testautopr ./...`

### Notes

- The project requires Go >= 1.22.3 (specified in `go.mod`).
- There are no databases, Docker services, or other infrastructure dependencies.
