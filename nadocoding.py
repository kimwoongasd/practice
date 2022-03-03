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
            
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 공격합니다. [공격력 {self.damage}]')
        
class Flyalbe:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed
        
    def move(self, name, location):
        print(f'{name} : {location} 방향으로 날아갑니다. [속도 {self.fly_speed}]')
        

class FlyableAttackUnit(AttackUnit, Flyalbe):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyalbe.__init__(fly_speed)