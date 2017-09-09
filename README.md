# NBA_DataVisualization

本项目采用了Python爬取NBA球员和球队数据，并使用Google Map API获取地理位置坐标数据
项目使用Tableau可视化软件进行可视化展示，Tableau真的功能强大


对Python源码感兴趣的小伙伴，需要修改geo.py文件，添加自己的API_KEY（科学上网，你懂得）。

## 具体步骤如下
### Windows下安装与使用
* 1.安装Anaconda(`https://www.anaconda.com/download/`)
* 2.打开Anaconda, 安装googleMapApi 版本为2.4.6，或者通过在【开始】【执行】pip install googlemaps

* 3.打开cmd窗口，定位到`SpiderNBA.py`所在的文件夹，执行
`python SpiderNBA.py`
* 4.找到输出的txt文件 `play_info.txt`, 因为可能不在当前目录下

* 5.申请Google Map APIKEY(`https://developers.google.com/maps/documentation/geocoding/start?hl=zh-cn`)
* 6.将申请到的API_KEY添加到`geo.py`API_KEY参数中
* 7.执行`python geo.py`，看到输出结果文件`team_location_info.txt`


### MacOS/Linux下的安装与使用
* 1.安装Anaconda(`https://www.anaconda.com/download/`)
* 2.打开Anaconda, 安装googleMapApi 版本为2.4.6，或者通过在【terminal】中执行 pip install googlemaps
* 3.将目录定向定位到`SpiderNBA.py`所在的文件夹，执行
`python SpiderNBA.py`
* 4.找到输出的txt文件 `play_info.txt`, 因为可能不在当前目录下

* 5.申请Google Map APIKEY(`https://developers.google.com/maps/documentation/geocoding/start?hl=zh-cn`)
* 6.将申请到的API_KEY添加到`geo.py`API_KEY参数中
* 7.执行`python geo.py`，看到输出结果文件`team_location_info.txt`
