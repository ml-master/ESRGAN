# ESRGAN
ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks
```bib
@inbook{
Wang_Yu_Wu_Gu_Liu_Dong_Qiao_Loy_2019,   title={ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks},  url={http://dx.doi.org/10.1007/978-3-030-11021-5_5},  DOI={10.1007/978-3-030-11021-5_5},  booktitle={Lecture Notes in Computer Science,Computer Vision – ECCV 2018 Workshops},  author={Wang, Xintao and Yu, Ke and Wu, Shixiang and Gu, Jinjin and Liu, Yihao and Dong, Chao and Qiao, Yu and Loy, Chen Change},  year={2019},  month={Jan},  pages={63–79},  language={en-US}  }
```
## Setup Environment
### Install required packages 
```shell
python3.9 pytorch1.12 cuda11.7 
torch>=0.4.0 torchvision matplotlib numpy scipy pillow urllib3 
scikit-image
pip install -r requirements.txt
```
## dataset

Super-resolution of CelebA using Generative Adversarial Networks.
The dataset can be downloaded from: https://www.dropbox.com/sh/8oqt9vytwxb3s4r/AADIKlz8PR9zr6Y20qbkunrba/Img/img_align_celeba.zip?dl=0
(if not available there see if options are listed at http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
Instrustion on running the script:
1. Download the dataset from the provided link
2. Save the folder 'img_align_celeba' to '../data/'
4. Run the sript using command 'python3 esrgan.py'

Download images from this link: Google Drive  from: https://drive.google.com/drive/folders/11okt9IRDxXgfTr7Ae1wxl9CHZC1PphhC
We also download the related images of the GossipCop dataset. We remove the invalid images.
The name rule of the image is {news_id}_top_img.png, such as gossipcop-541230_top_img.png.


## 结果
### Celea  
<img src="https://github.com/ml-master/ESRGAN/blob/main/image.png" width="800" height="300" />  

### 新闻数据集 We also download the related images of the GossipCop dataset  result 
<img src="https://github.com/ml-master/ESRGAN/blob/main/result_top_img.png" width="800" height="300" />  
### 对比试验
<img src="https://github.com/ml-master/ESRGAN/blob/main/对比实验.png" width="800" height="400" />  
### 插值函数系数影响结果对比
<img src="https://github.com/ml-master/ESRGAN/blob/main/插值函数系数影响结果对比.png" width="800" height="300" /> 
### 消融实验
<img src="https://github.com/ml-master/ESRGAN/blob/main/消融实验.png" width="800" height="400" />  
<img src="https://github.com/ml-master/ESRGAN/blob/main/消融实验结果.png" width="800" height="400" />  

