import sys
import simpy
from flask import Flask, request, jsonify
import ZDJ

app = Flask(__name__)

url = None

@app.route('/process-data', methods=['POST'])
def handle_request():
    # 尝试解析JSON数据
    data = request.get_json()

    # response=requests.get(url)
    INITIAL_LENGTH = [11209.24, 39902.07, 12082.64, -0.72, 21325.83, 12456.52, 77362.71, 1.98]
    ZDJ_SPEED_STYLE = 1  # 折叠机速度样式(0表示通过工作时间转换，1表示直接用速度值)
    TIME_One_DZ = 0  # 折叠机生产一个长条纸叠需要的时间
    TIME_ZD_MOVE = 5  # 长条纸叠在折叠机移动需要的时间
    TIME_SPEED_CHANGE = [0.0, 1.019, 2.036, 3.059, 5.092, 6.111, 10.18, 11.197, 12.213, 13.233, 15.27, 17.306, 1135.693,
                         1136.708, 1203.913, 1204.931, 1319.965, 1320.984, 1597.721, 1598.737, 1599.753, 1600.774,
                         1601.788, 1602.804, 1603.822, 1604.838, 1605.855]
    SPEED_CHANGE = [1.75, 1.8333333333333333, 1.9, 1.9333333333333333, 1.9666666666666666, 2.05, 2.1,
                    2.1333333333333333, 2.15, 2.183333333333333, 2.2333333333333334, 2.2666666666666666, 2.25,
                    2.2333333333333334, 2.2, 2.183333333333333, 2.1666666666666665, 2.183333333333333,
                    2.066666666666667, 1.8833333333333333, 1.7, 1.5166666666666666, 1.3333333333333333, 1.15,
                    0.9666666666666667, 0.7833333333333333, 0.75]
    # NO_OF_SHEETS = 100  # 抽数
    # LENGTH_OF_SHEETS = 0.195  # 每抽长度
    SIM_TIME = 1616

    control_signals = data.get('control', {}).get('signalList', [])

    # 初始化用于存储提取值的变量
    NO_OF_SHEETS = None
    LENGTH_OF_SHEETS = None

    for signal in control_signals:
        if signal.get('applicationPropertyIdentifier') == 'noOfSheets':
            NO_OF_SHEETS = float(signal.get('value'))
        elif signal.get('applicationPropertyIdentifier') == 'lengthOfSheet':
            LENGTH_OF_SHEETS = float(signal.get('value'))

    env=simpy.Environment()
    zdj= ZDJ.ZDJ()
    env.process(ZDJ.product_ctzd(env,zdj,INITIAL_LENGTH,ZDJ_SPEED_STYLE,TIME_One_DZ,TIME_SPEED_CHANGE,SPEED_CHANGE,NO_OF_SHEETS,LENGTH_OF_SHEETS,TIME_ZD_MOVE))
    env.run(until=SIM_TIME)

    # 仿真结果json输出
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

    print("折叠机入包数",zdj.DATA_LIST_ZJ_RBS)
    # print("折叠机出包数",zdj.zdj_cbs_list)
    # print("剩余原纸长度=",zdj.paperLength_list)

    return jsonify(response_data)

def main():
    global url
    if len(sys.argv) != 3:
        print("Usage: python MAIN.py <url> <port>")
        sys.exit(1)

    url = sys.argv[1]
    port = int(sys.argv[2])

    print(f"Starting Flask server at {url}:{port}")
    app.run(host='0.0.0.0', debug=True, port=port)


if __name__ == '__main__':
    main()



 
 
