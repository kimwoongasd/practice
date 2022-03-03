class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{name} 유닛이 생성 되었습니다')
        
    def move(self, location):
        print(f'[지상 유닛 이동] {self.namae} : {location} 방향으로 이동합니다. [속도 {self.speed}]')
        
    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입었습니다.')
        self.hp -= damage
        if self.hp > 0:
            print(f'{self.name} : 현재 체력은 {self.hp}입니다.')
        
        else:
            print(f'{self.name} 유닛이 파괴 되었습니다.')