# 주어진 코드를 활용하여 부동산 프로그램 작성
# 출력 예제
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 매매 5억 2017년
# 송파 빌라 월세 500/50 2020년

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print(f'{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}')


house_1 = House('강남', '아파트', '매매', '10억', '2010년')
house_2 = House('마포', '오피스텔', '매매', '5억', '2017년')
house_3 = House('송파', '빌라', '월세', '500/50', '2020년')

house_1.show_detail()
house_2.show_detail()
house_3.show_detail()