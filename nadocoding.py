class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{name} 유닛이 생성 되었습니다')
        
    def move(self, location):
        print(f'[지상 유닛 이동] {self.namae} : {location} 방향으로 이동합니다. [속도 {self.speed}]')