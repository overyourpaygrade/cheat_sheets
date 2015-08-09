###### Hide a file (if pass = y AES encrypted)
* steghide embed -cf picture.jpg -ef text.txt

###### Info on the image (size to embedd)
* steghide image.jpg

###### Extract hidden file from file
* steghide extract -sf picture.jpg
