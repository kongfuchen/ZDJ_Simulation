# ZDJ_Simulation

仿真模型库基于python3编写，需要正常使用，请先确保以下python包正常安装：  
    1. simpy  
    2. flask  
    3. sys  
 
MAIN.py为主文件，主要功能为：  
    1. 接收并解析传过来的json数据  
    2. 将解析完的json数据传入仿真模型并开启仿真  
    3. 以json数据格式返回仿真结果  

ZDJ.py为折叠机仿真的类文件

post_json.py为向MAIN.py发送"AI接收数据结构新.json"格式的json数据，为了测试MAIN.py是否能正常接收并解析json数据

调用时只需要运行MAIN.py脚本，但请传入URL与端口号

比如，像post_json.py中将数据发送到'http://localhost:5000/process-data'  
http://localhost 表示服务器在本地主机上运行。
5000 表示服务器监听的端口号是5000。
/process-data 是服务器上用来处理数据的具体路径。

启动python脚本时：

python MAIN.py http://localhost 5000

MAIN.py的路径设置为默认路径/process-data

请先启动python脚本，再向脚本发送json数据，如果能够正常接收json数据并仿真，会返回
    response_data={  
      "list": [  
        {  
          #方案编码  
          "simulationSchemeCode": "1",  
          #实体编码  
          "entityIdentifier": "22_cx_D_zdj",  
          #属性编码  
          "applicationPropertyIdentifier": "186_D2001",  
          #值  
          "values": ["10","8","12","null","null","null"],  
          #日期  
          "times": ["2024-07-24 09:30:00","2024-07-24 09:31:00","2024-07-24 09:32:00","2024-07-24 09:33:00","2024-07-24 09:34:00","2024-07-24 09:35:00"]  
        }  
      ]  
    }  
  的json数据。



