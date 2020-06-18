- [x] satuin gambar, dengan cara cari seluruh format gambarnya pake glob, terus pindahin ke satu folder aja 
- [x] search duplicated dataset with phash
- [ ] buat model untuk cek ini sertif yang beneran apa nggak -> simple cnn would do i guess?
- [ ] training pipeline di kedro


see you in a month. lol.
![training has begun see you in 10 days](https://i.imgur.com/Bh2i0zU.png)
training is actually done, first batch evaluations are: 
- log loss didn't converge
	- images are too "unique"
	- incosistent padding / whitespaces that surrounds the image
		- ![](https://i.imgur.com/lTDK9Qy.png)
fixes to do: 
- [ ] sertifikat classifier
- [ ] gak usah di dedupe, 'agak mirip' is fine -> set the threshold to be >=2 
- [ ] re-label the sertifikat classifier images, for a better criteria
