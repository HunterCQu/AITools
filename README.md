# 脚本工具箱
- copyfiles.py ： 文件/文件夹复制脚本
- create_txt_list.py ： VOC数据集main/train.txt等txt制作脚本
    ```
    input: python create_txt_list.py "/home/andy/Data/"
    output: 
        ./train.txt
        ./val.txt
    ```
- showprocessbar.py ： 显示处理进度脚本
- pick_all_xml_img.py ： 从同一个文件夹中挑选xml和image文件分别到相应文件夹中
    ```
    input: python pick_all_xml_img.py "/home/andy/data/img"
    output:    
        ./pickedLabel
        ./pickedImg
    ```
- pick_txt_img_by_label.py : 根据指定标签将txt和image文件挑出来
    ```
    input : python pick_txt_img_by_label.py  "/home/andy/data/label_dir/"  "/home/andy/data/img_dir/" 
    output : 
        ./pickedLabel
        ./pickedImg
    ```
- txt2xml.py ： YOLO的txt标签转VOC的xml格式标签脚本
    ```
    input : python txt2xml.py "/home/andy/data/ann_dir" "/home/andy/data/img_dir"
    output:
        ./xml
    ```
- xml2txt.py　：　VOC数据集xml标签转YOLO需要的txt格式的标签脚本