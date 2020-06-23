

mkdir "jpg" "png" "tiff"

ls

find -type f -name "*jpg"
find -type f -name "*tiff"
find -type f -name "*png"

find . -type f -name *.jpg -exec cp {} ./JPG/ \;
find . -type f -name *.png -exec cp {} ./PNG/ \;
find . -type f -name *.tiff -exec cp {} ./TIFF \;

echo "JPG Count " > picturecounts.md
find ./JPG -type f -iname *.jpg | wc -l >> picturecounts.md
echo "PNG Count " > picturecounnts.md
find ./PNG -type f -iname *.png | wc -l>> picturecount.md
echo "TIFF Count " > picturecount.md
find ./TIFF -type f -iname *.tiff | wc -l >> picturecount.md


