import requests
import json
import requests
import json

url = 'http://localhost:5000/process-data'

# 定义要发送的 JSON 数据
data = {
  #初始化参数
  "init": {
    "signalList": [
      {
        "applicationPropertyIdentifier": "150_D20316",
        "dataSourceType": "iot",
        "entityIdentifier": "22_cx_D_yzj_1",
        "times": [
          "2024-07-24 09:30:00",
          "2024-07-24 09:31:00"
        ],
        "values": [
          "100.0",
          "80.0"
        ]
      },
      {
        "applicationPropertyIdentifier": "150_D20318",
        "dataSourceType": "person",
        "entityIdentifier": "22_cx_D_yzj_2",
        "value": "100.0"
      }
    ]
  },
  #控制参数
  "control": {
    "signalList": [
      {
        "applicationPropertyIdentifier": "noOfSheets",
        "dataSourceType": "person",
        "entityIdentifier": "22_cx_D_zdj",
        "value": "195"
      },
      {
        "applicationPropertyIdentifier": "lengthOfSheet",
        "dataSourceType": "person",
        "entityIdentifier": "22_cx_D_zdj",
        "value": "100"
      }
    ]
  },
  #输入参数
  "input": {
    "signalList": [
      {
        "applicationPropertyIdentifier": "150_D20316",
        "dataSourceType": "iot",
        "entityIdentifier": "22_cx_D_yzj_1",
        "times": [
          "2024-07-24 09:30:00",
          "2024-07-24 09:31:00"
        ],
        "values": [
          "100.0",
          "80.0"
        ]
      },
      {
        "applicationPropertyIdentifier": "186_D2001",
        "dataSourceType": "iot",
        "entityIdentifier": "22_cx_D_zdj",
        "times": [
          "2024-07-24 09:30:00",
          "2024-07-24 09:31:00"
        ],
        "value": "",
        "values": [
          "10",
          "8"
        ]
      },
      {
        #加工时间, 手动输入
        "applicationPropertyIdentifier": "processTime",
        "dataSourceType": "person",
        "entityIdentifier": "22_cx_D_zdj",
        "value": ""
      },
      #传输时间
      {
        "applicationPropertyIdentifier": "transportTime",
        "dataSourceType": "person",
        "entityIdentifier": "22_cx_D_zdj",
        "value": ""
      }
    ]
  },
  "output": {
    "signalList": [
      {
        #纸叠条数
        "applicationPropertyIdentifier": "StripPaperStack",
        "dataSourceType": "ai",
        "entityIdentifier": "22_cx_D_zdj",
        "value": ""
      }
    ]
  }
}
# 发送 POST 请求
response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

print(response.text)

# # 打印响应
# print("Response from server:", response)

# url = 'http://localhost:5000/phantom-platform-data/api/v1.8/simulation/save'
#
# data={
#     "list": [
#         {
#             "simulationSchemeCode": "1",
#             "entityIdentifier": "22_cx_D_zdj",
#             "applicationPropertyIdentifier": "186_D2001",
#             "values": [
#                 "10",
#                 "8",
#                 "12",
#                 "null",
#                 "null",
#                 "null"
#             ],
#             "times": [
#                 "2024-07-24 09:30:00",
#                 "2024-07-24 09:31:00",
#                 "2024-07-24 09:32:00",
#                 "2024-07-24 09:33:00",
#                 "2024-07-24 09:34:00",
#                 "2024-07-24 09:35:00"
#             ]
#         }
#     ]
# }
#
# # 将数据转换为JSON格式
# json_data = json.dumps(data)
#
# # 发送POST请求
# response = requests.post(url, headers={"Content-Type": "application/json"}, data=json_data)
#
# # 打印响应
# print("Response from server:", response.text)
