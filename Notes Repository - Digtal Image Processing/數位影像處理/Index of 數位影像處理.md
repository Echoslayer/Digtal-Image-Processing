- 基本資訊
	- 作者: Rafael C. Gonzalez, Richard E. Woods
	- 版本: Third Edition

--- 

## 第一章　緒論
- One picture is worth more than ten thousand words.(Anonymous)
- 影像處理的基本步驟
	- 影像擷取
		- ch02
	- 影像增強
		- ch02, ch03, ch04
	- 影像復原
		- ch05
	- 彩色影像處理
		- ch06 
	- 小波
		- ch07
	- 壓縮
		- ch08
	- 形態學處理
		- ch09
	- 分割
		- ch10
	- 表示與描述
		- ch11
	- 辨識
		- ch12
## 第二章　數位影像基礎
- Those who wish to succeed must ask the right preliminary questions. (Aristotle)
- 取像方式有多種: 單一感應器、長條、陣列、線取像
- 連續感應的資料需要經過兩個過程將資料轉化為數位的形式: 取樣(Sampling)與量化(Quantization)
	- 取樣: 將座標數值化
	- 量化: 將振幅數值化
- 數位影像的品質取決於用在取樣和離散強度準位的數目 
- 空間解析度: [[Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007).pdf#page=82&selection=241,8,245,34|Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007), 第 82 頁]]
	- 每單位距離有幾條線
	- 每單位距離的點(像素)數
	- 每英吋的點數(Dots per inch, dpi)
- 強度解析度
	- 最小可分辨的強度準位變化
	- 2的整數次方，因為儲存方便
- 影像內插: 將影像空間解析度放大的方式(有幾種不同的方式)
- 像素的一些基本關係
	- 近鄰 [[Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007).pdf#page=92&selection=445,0,446,1|Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007), 第 92 頁]] 
		- 4近鄰(4-neighbor): 十字
		- 8近鄰(8-neighbor): 米字
		- 鄰接性 
			- 8-鄰接的像素可能會通過對角線方向的連接產生不需要的連通區域，而m-鄰接可以避免這種情況
		- 連通性
			- 連通的
			- 連通成分
			- 連通集合
		- 區域
			- 連通集合
		- 邊界
			- 內邊界與外邊界
	- 距離
		- 歐幾里得距離
		- 市街距離
		- 棋盤距離
- 影像運算
	- 是點乘積
	- 細節增強 [[Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007).pdf#page=100&selection=8,0,9,0|Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007), 第 100 頁]]
	- 集合與邏輯運算 [[Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007).pdf#page=103&selection=26,1,27,26|Rafael C. Gonzalez, Richard E. Woods - Digital Image Processing-Pearson (2007), 第 103 頁]]
	- 模糊集合
	- 空間運算
		- 直接在影像的像素上執行，有三種
			- 單一像素運算
			- 鄰域運算
			- 幾何空間轉換
				- forward mapping
				- inverse mapping
				- 解決誤差: 運用連接點(tie point)，人造物會建立網格標記(reseau mark)
## 第三章　強度轉換與空間濾波
- It makes all the difference whether one sees darkness through the light or brightness through the shadows. (David Lindsay)
## 第四章　頻率域上的濾波
- Filter: A device or material for suppressing or minimizing waves or oscillations of certain frequencies. Frequency: The number of times that a periodic function repeats the same sequence of values during a unit variation of the independent variable. (Webster’s New Collegiate Dictionary)
## 第五章　影像復原與重建
- Things which we see are not by themselves what we see. It remains completely unknown to us what the objects may be by themselves and apart from the receptivity of our senses. We know nothing but our manner of perceiving them. (Immanuel Kant)
## 第六章　彩色影像處理
- It is only after years of preparation that the young artist should touch color—not color used descriptively, that is, but as a means of personal expression. Henri Matisse For a long time I limited myself to one color—as a form of discipline. (Pablo Picasso)
## 第七章　小波和多解析度處理
- All this time, the guard was looking at her, first through a telescope, then through a microscope, and then through an opera glass. (Lewis Carrol, Through the Looking Glass)
## 第八章　影像壓縮
- But life is short and information endless Abbreviation is a necessary evil and the abbreviator’s business is to make the best of a job which, although intrinsically bad, is still better than nothing. (Aldous Huxley)
## 第九章　形態學影像處理
- In form and feature, face and limb, I grew so like my brother That folks got taking me for him And each for one another. (Henry Sambrooke Leigh, Carols of Cockayne, The Twins)
## 第十章　影像分割
- The whole is equal to the sum of its parts. (Euclid) 
- The whole is greater than the sum of its parts. (Max Wertheimer)
## 第十一章　表示與描述
- Well, but reflect; have we not several times acknowledged that names rightly given are the likenesses and images of the things which they name? (Socrates)
## 第十二章　物體辨識
- One of the most interesting aspects of the world is that it can be considered to be made up of patterns. A pattern is essentially an arrangement. It is characterized by the order of the elements of which it is made, rather than by the intrinsic nature of these elements. (Norbert Wiener)
- 影像壓縮用的編碼表
	- 

