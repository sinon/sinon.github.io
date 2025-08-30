+++
title = "TIL: Cleaning exif data from images"
date = 2024-10-24
[taxonomies]
tags = ["til", "exif", "blogging"]
+++

When uploading images to blog from phone need to remove GPS and other private metadata. For the blog I use [ExifTool](https://exiftool.org/) running `exiftool -gps:all= static/*.jpg`