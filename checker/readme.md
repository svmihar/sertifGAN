# sertif bagus classifier

achieves automated filter for a good certificate or not, based on my labels.
 (you can too)

## labelling
jupyter innotater on raw scraped images, see [jupyter notebook here](/path/to/ipynb)   
i sampled ~500 images with 'sertifikat' and 'bukan_sertifikat'    
sertifikat are images with certain criteria listed below: 
- 16:9 aspect ratio 
- has a clear characteristics of a certificate like: name, decorations, stamps and etc.
- doesn't have any "watermarks": website on the edges, samples, those dirty stock photos watermarking
- big ass margin on the certificates -> this creates a incosistent log loss on stylegan2, gotta make the certificate nice and center without any margin / whitespaces took me fucking 8 days to sort this out.

while the 'bukan_certificate' are the images that doesn't met the criteria above. pretty straightforward


## model arch 
achieved with fastai's model classifier

## todos
- [x] label-studio slur
- [ ] training  on new sampled images
