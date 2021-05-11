# -*- coding:utf-8 -*-
# list + dict + 객체

student = [[90, 50], [80, 60], [60, 30]]
print(student[0])  # 첫번째 학생의 모든 점수
print(student[0][1])  # 첫번째 학생의 두번째 점수 데이터

student2 = {"홍길동":[90, 50], "김길동":[80, 60], "이길동":[60, 30]}

print(student2["홍길동"])  # 홍길동의 모든 점수 
print(student2["홍길동"][1])  # 홍길동의 두번째 점수 데이터 / dict안에 value값이 list인 데이터

student3 = {
            "홍": {"중간":90, "기말":50},
            "이": {"중간":80, "기말":60},
            "이": {"중간":60, "기말":30}  # dict안에 dict로 구성
            }
print(student3["홍"]["기말"])  # 홍의 기말점수데이터 / dict안에 dict로 구성된 데이터로 만들어야 함

student4 = [
            {"중간":90, "기말":50}, 
            {"중간":80, "기말":60},
            {"중간":60, "기말":30}
            ]
print(student4[0]["기말"])    # list안에 dict가 요소 값으로 가진 데이터로 만들어야 함
print("---------------")

air = {"RealtimeCityAir":{"list_total_count":25,"RESULT":{"CODE":"INFO-000","MESSAGE":"정상 처리되었습니다"},"row":[{"MSRDT":"202105111500","MSRRGN_NM":"도심권","MSRSTE_NM":"중구","PM10":25.0,"PM25":9.0,"O3":0.048,"NO2":0.022,"CO":0.4,"SO2":0.001,"IDEX_NM":"보통","IDEX_MVL":66.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"도심권","MSRSTE_NM":"종로구","PM10":20.0,"PM25":10.0,"O3":0.053,"NO2":0.014,"CO":0.4,"SO2":0.004,"IDEX_NM":"보통","IDEX_MVL":70.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"도심권","MSRSTE_NM":"용산구","PM10":21.0,"PM25":6.0,"O3":0.047,"NO2":0.01,"CO":0.3,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":65.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서북권","MSRSTE_NM":"은평구","PM10":11.0,"PM25":6.0,"O3":0.062,"NO2":0.007,"CO":0.3,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":77.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서북권","MSRSTE_NM":"서대문구","PM10":19.0,"PM25":11.0,"O3":0.056,"NO2":0.009,"CO":0.4,"SO2":0.004,"IDEX_NM":"보통","IDEX_MVL":72.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서북권","MSRSTE_NM":"마포구","PM10":16.0,"PM25":6.0,"O3":0.048,"NO2":0.012,"CO":0.3,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":66.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"광진구","PM10":19.0,"PM25":6.0,"O3":0.05,"NO2":0.008,"CO":0.3,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":67.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"성동구","PM10":19.0,"PM25":8.0,"O3":0.062,"NO2":0.019,"CO":0.3,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":77.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"중랑구","PM10":42.0,"PM25":9.0,"O3":0.048,"NO2":0.013,"CO":0.3,"SO2":0.004,"IDEX_NM":"보통","IDEX_MVL":66.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"동대문구","PM10":15.0,"PM25":7.0,"O3":0.053,"NO2":0.012,"CO":0.3,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":70.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"성북구","PM10":20.0,"PM25":6.0,"O3":0.05,"NO2":0.014,"CO":0.5,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":67.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"도봉구","PM10":17.0,"PM25":5.0,"O3":0.053,"NO2":0.007,"CO":0.2,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":70.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"강북구","PM10":17.0,"PM25":7.0,"O3":0.056,"NO2":0.008,"CO":0.2,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":72.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동북권","MSRSTE_NM":"노원구","PM10":18.0,"PM25":3.0,"O3":0.052,"NO2":0.008,"CO":0.3,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":69.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"강서구","PM10":16.0,"PM25":9.0,"O3":0.055,"NO2":0.012,"CO":0.3,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":71.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"구로구","PM10":33.0,"PM25":6.0,"O3":0.054,"NO2":0.011,"CO":0.3,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":71.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"영등포구","PM10":17.0,"PM25":5.0,"O3":0.046,"NO2":0.017,"CO":0.4,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":64.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"동작구","PM10":24.0,"PM25":8.0,"O3":0.051,"NO2":0.011,"CO":0.3,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":68.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"관악구","PM10":24.0,"PM25":8.0,"O3":0.047,"NO2":0.016,"CO":0.4,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":65.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"금천구","PM10":30.0,"PM25":17.0,"O3":0.053,"NO2":0.011,"CO":0.4,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":70.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"서남권","MSRSTE_NM":"양천구","PM10":25.0,"PM25":8.0,"O3":0.049,"NO2":0.013,"CO":0.4,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":66.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동남권","MSRSTE_NM":"강남구","PM10":22.0,"PM25":10.0,"O3":0.051,"NO2":0.014,"CO":0.4,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":68.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동남권","MSRSTE_NM":"서초구","PM10":28.0,"PM25":2.0,"O3":0.048,"NO2":0.019,"CO":0.3,"SO2":0.004,"IDEX_NM":"보통","IDEX_MVL":66.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동남권","MSRSTE_NM":"송파구","PM10":23.0,"PM25":14.0,"O3":0.054,"NO2":0.014,"CO":0.4,"SO2":0.003,"IDEX_NM":"보통","IDEX_MVL":71.0,"ARPLT_MAIN":"O3"},{"MSRDT":"202105111500","MSRRGN_NM":"동남권","MSRSTE_NM":"강동구","PM10":23.0,"PM25":9.0,"O3":0.048,"NO2":0.009,"CO":0.3,"SO2":0.002,"IDEX_NM":"보통","IDEX_MVL":66.0,"ARPLT_MAIN":"O3"}]}}
# print(air.keys())
# print(air.values())
# print(air["RealtimeCityAir"]["row"])
# city = list(air["RealtimeCityAir"]["row"])       
# print("두번째 도시의 PM10 : " + str(city[1]["PM10"]))
# print("세번째 도시의 PM25 : " + str(city[2]["PM25"]))
# print(city[1]["PM10"])
# print(city[2]["PM25"])

print(air["RealtimeCityAir"]["row"][1]["PM10"])     # 두번째 도시 PM10
print(air["RealtimeCityAir"]["row"][2]["PM25"])     # 세번째 도시 PM25
print(air["RealtimeCityAir"]["row"][24]["IDEX_NM"])     
print(air["RealtimeCityAir"]["row"][-1]["IDEX_NM"])     # 마지막 도시 상태

wData = {"coord":{"lon":126.9778,"lat":37.5683},"weather":[{"id":800,"main":"Clear","description":"맑음","icon":"01d"}],"base":"stations","main":{"temp":25.53,"feels_like":24.66,"temp_min":22.64,"temp_max":26.64,"pressure":1011,"humidity":20,"sea_level":1011,"grnd_level":1005},"visibility":10000,"wind":{"speed":4.92,"deg":134,"gust":6.27},"clouds":{"all":0},"dt":1620716801,"sys":{"type":1,"id":8105,"country":"KR","sunrise":1620678396,"sunset":1620729024},"timezone":32400,"id":1835848,"name":"Seoul","cod":200}

l = wData["weather"]
d = l[0]
desc = d["description"]
print(desc)

print(wData["weather"][0]["description"])   #날씨
print(wData["main"]["temp"])                # 기온
print(wData["main"]["humidity"])            # 습도
print(wData["main"]["feels_like"])          # 체감온도












