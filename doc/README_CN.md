# mask-converter

將JSON文件（VIA 2的結果）中的輪廓轉換為PNG文件掩膜

# 1. 簡介

## 關於VIA 2

[VIA 2](https://www.robots.ox.ac.uk/~vgg/software/via/) 是一個基於網頁應用的圖像標註工具，用於創建和管理圖像的
標註。它由牛津大學視覺幾何組（Visual Geometry Group，VGG）的 Abhishek Dutta、Ankush Gupta 和 Andrew
Zisserman 開發。

VIA工具允許用戶使用邊界框、多邊形、線條和點等對象類型對圖像進行標註。它還支持多種標註格式，包括COCO、JSON和CSV，使其成為
各種計算機視覺任務（如目標檢測、分割和識別）的通用工具。

## mask-converter 可以做什麼

如果您像我一樣正在為圖像分割演算法標註圖像，可能也會發現，來自 VIA 2 的 JSON 數據不適合用於像 U-Net 這樣的分割模型。
mask-converter 可以將 JSON 數據轉換為 PNG 掩膜，非常適合用於模型訓練。

# 2. 使用方法

所需軟體：
- 作業系統系統：Windows
- 軟體：VIA（版本 2.0.*）

工作流程：
1. 在開始標註過程之前，請確保您打算標註的所有圖像已經整理並存儲在同一個文件夾中。
2. 使用 VIA 2 為您的圖像生成標註並保存為 JSON 文件。
3. 雙擊運行程序 "mask-converter.exe" 。
4. 根據程序提示，導航到包含要標註圖像的文件夾。
5. 接下來，選擇由 VIA 2 生成的 JSON 文件，然後點擊 "確定" 開始轉換過程。
