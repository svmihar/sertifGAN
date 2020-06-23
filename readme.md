- [x] satuin gambar, dengan cara cari seluruh format gambarnya pake glob, terus pindahin ke satu folder aja
- [x] search duplicated dataset with phash
- [x] buat model untuk cek ini sertif yang beneran apa nggak -> simple cnn would do i guess?
- [ ] training pipeline di kedro

# dataset
- semua, full size, >90 accuracy on sertif_clf
	- [sertifikat.zip (restricteD)](https://drive.google.com/file/d/1o6SM3Iq6KN0WrmYA6Mp3HwjRFmh9u-n7/view?usp=sharing)
- resized, non transparent, converted to 512*512
	- [sertifikat_resized.zip (restricted)](https://drive.google.com/file/d/1W-Iz_I__7oh5Qm1QA7QOX1NeAn7kZtYg/view?usp=sharing)


see you in a month. lol.
![training has begun see you in 10 days](https://i.imgur.com/Bh2i0zU.png)
### batch #1
training is actually done, first batch evaluations are:
- log loss didn't converge
	- images are too "unique"
	- incosistent padding / whitespaces that surrounds the image
		- ![](https://i.imgur.com/lTDK9Qy.png)
	- karena di paksa resize 512 * 512, some vertical aspect ratio certificate got squished. guess will try to find them and ~~kill~~ delete them

### batch #2
fixes to do:
- [x] sertifikat classifier
- [x] gak usah di dedupe, 'agak mirip' is fine -> set the threshold to be >=2
- [x] re-label the sertifikat classifier images, for a better criteria
- [x] watch dog kalo model udah selesai training -> upload ke drive
- [x] watch dog biar modelnya yang disimpen cuman 2 aja 
