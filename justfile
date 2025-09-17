clean-gps:
  exiftool -gps:all= static/*.jpg

lint:
  uvx codespell -I .codespellignore content/
  lychee -v content/*.md
pylint:
  uvx ruff format scripts
  uvx ruff check scripts
  uvx pyrefly check scripts