.PHONY: clean-gps

clean-gps:
  exiftool -gps:all= static/*.jpg