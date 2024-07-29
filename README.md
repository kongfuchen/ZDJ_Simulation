# ZDJ_Simulation

调用时请传入URL与端口号

比如，将数据发送到'http://localhost:5000/process-data'
启动python脚本时：

python MAIN.py http://localhost 5000

http://localhost 表示服务器在本地主机上运行。
:5000 表示服务器监听的端口号是5000。
/process-data 是服务器上用来处理数据的具体路径。

MAIN.py的路径设置为默认路径/process-data

请先启动python脚本，再向脚本发送json数据，如果能够正常仿真运行，会返回
    response_data={
      \\"list": [
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
  的json文件。



