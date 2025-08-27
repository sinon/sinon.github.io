clean-gps:
  exiftool -gps:all= static/*.jpg

lint:
  uvx codespell -I .codespellignore content/
  lychee -v content/*.md