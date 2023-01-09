#!/usr/bin/python3
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import os
import ntpath
import hashlib
import copy


from ui import mainWindow


def checksum(filename, hash_factory=hashlib.md5, chunk_num_blocks=128):
    h = hash_factory()
    with open(filename, 'rb') as f:
        while chunk := f.read(chunk_num_blocks*h.block_size):
            h.update(chunk)
    return h.hexdigest()


def get_same_file(root_path, file_list, dir_list, same_file, min_size=0):
    # 获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):  # 目录
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            get_same_file(dir_file_path, file_list, dir_list, same_file)
        else:  # 文件
            if (os.path.getsize(dir_file_path)*0.000001) >= min_size:  # 判断是否超过了最小大小
                file_list.append(dir_file_path)
                if dir_file in same_file:
                    same_file[dir_file].append(dir_file_path)
                    # print(same_file[dir_file])
                else:
                    same_file[dir_file] = [dir_file_path]


def check_files(v, same_file_md5):
    for i in v:
        # print(i)
        if checksum(i) in same_file_md5.keys():
            same_file_md5[checksum(i)].append(i)
        else:
            same_file_md5[checksum(i)] = [i]
    temp = copy.copy(same_file_md5)
    for k, v in temp.items():
        if len(v) == 1:
            same_file_md5.pop(k)
    return same_file_md5


def scan(url, quickly=True, min_size=0):
    # same_file_md5 结构 “md5”:["第一个文件路径"，"第二个文件路径"，"第三个文件路径"，……]
    same_file_md5 = {}

    # 结构  "文件名":["第一个文件路径"，"第二个文件路径"，"第三个文件路径"，……]
    same_file = {}

    # 用来存放所有的文件路径
    file_list = []
    # 用来存放所有的目录路径
    dir_list = []

    get_same_file(url, file_list, dir_list, same_file)

    # print(file_list)

    if quickly:
        same_file = list(same_file.values())
        for v in same_file:
            if len(v) <= 1:
                # same_file.remove(v)
                continue
            check_files(v, same_file_md5)
    else:

        check_files(file_list, same_file_md5)

    print(same_file_md5)
    return same_file_md5


class main(QMainWindow, mainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(True)

        self.pushButton.clicked.connect(self.link_file)
        self.pushButton_2.clicked.connect(self.q_scan)
        self.start_scan.clicked.connect(self.n_scan)

    def link_file(self):
        for j in list(self.same_file_md5.values()):
            for i in j[1:]:
                print(i)
                os.remove(i)
                os.link(j[0], i)

    def q_scan(self):  # 快扫
        self.link = self.links.text()
        self.min_size_num = self.min_size.text()
        self.same_file_md5 = scan(self.link, True, int(self.min_size_num))
        self.fill_table(self.same_file_md5)

    def n_scan(self):  # 快扫
        self.link = self.links.text()
        self.min_size_M = int(self.min_size.text())
        self.same_file_md5 = scan(self.link, False, self.min_size_M)
        self.fill_table(self.same_file_md5)

    def fill_table(self, same_file_md5):
        # same_file_md5 结构 “md5”:["第一个文件路径"，"第二个文件路径"，"第三个文件路径"，……]
        for k, v in same_file_md5.items():
            # 增加一行
            # row = self.tableWidget.currentRow()
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            # 增加Md5、文件大小信息
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(k)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(
                str(os.path.getsize(v[0]))+"M"))

            # 增加一行中每个元素
            self.tableWidget.setColumnCount(len(v)+2)  # 增加列数
            for i in range(len(v)):
                item = QTableWidgetItem("文件"+str(i+1))
                self.tableWidget.setHorizontalHeaderItem(i+2, item)
                item = QTableWidgetItem(str(v[i]))
                self.tableWidget.setItem(row, i+2, item)
                print(row, i+2, str(v[i]))

            # 根据内容自动调整单元格大小
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()


app = QApplication(sys.argv)
window = main()
window.show()
# scan("/home/tim/TX/", False)
sys.exit(app.exec_())
