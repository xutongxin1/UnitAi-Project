又开始了新操作
excel 在python中的读取操作

基础包：xlrd
```
pip installxlrd
```
## 1.读取一个新的excel
```python
import xlrd
x1 = xlrd.open_workbook("123.xlse")
#打开文件
```
简单粗暴

## 2.读取一个sheet(工作表)
```python
x1.sheet_names()  # 获取所有sheet名字
x1.nsheets        # 获取sheet数量
x1.sheets()       # 获取所有sheet对象
x1.sheet_by_name("test")  # 通过sheet名查找
```

进入工作表
```python
sheet1=x1.sheet_by_name("test")
```
读取工作表中有关的数据
```python
sheet1.name   # 获取sheet的名字
sheet1.nrows  # 获取总行数
sheet1.ncols  # 获取总列数
```
## 3.读取单元格内容
```python
