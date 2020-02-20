# How to install package    

```bash
python -m pip install -r requirements.txt
```

# How to run   

```bash
python main.py -h    
usage: main.py [-h] [--list] [--updateDB UPDATEDB] [--support] [--checkUpdate]
               [--checkVulnerable]

optional arguments:
  -h, --help           show this help message and exit
  --list               List all installed program
  --updateDB UPDATEDB  Update newest version into Database
  --support            List application support by this project
  --checkUpdate        Check update for supported applications
  --checkVulnerable    Search CVEdetails about installed version
```
# List of options    

### List :   
Liệt kê tất cả chương trình đã được cài đặt trong máy mà project này hỗ trợ, đồng thời update file ```Database/current_version.json```.     

![](/img/hinh1.PNG)   


### UpdateDB :    
Update newest version trong file ```Database/new_version.json```.    

![](/img/hinh2.PNG)   


### support :    
Liệt kê tất cả các chương trình mà project này hỗ trợ.   

![](/img/hinh3.PNG)   


### checkUpdate :     
Liệt kê tất cả chương trình có thể update lên phiên bản cao hơn.    

![](/img/hinh4.PNG)   


### checkVulnerable :   
Liệt kê tất cả lỗ hổng của phiên bản hiện tại, nếu mà không có in ra ```No vulnerable```.    

![](/img/hinh5.PNG)   


