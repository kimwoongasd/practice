from random import *
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{name} 유닛이 생성 되었습니다')
        
    def move(self, location):
        print(f'{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]')
        
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
        
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f'{self.name} : 스팀팩을 사용합니다. (Hp 10 감소)')
        
        else:
            print(f'{self.name} : 체력이 부족하여 스팀팩을 사용하지 못합니다.')

class Tank(AttackUnit):
    seize_delveloped = False
    
    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.seize_mode = False
        
    def set_seize_mode(self):
        if Tank.seize_delveloped == False:
            return
        
        if self.seize_mode == False:
            print(f'{self.name} : 시즈모드로 전환합니다.')
            self.damage *= 2
            self.seize_mode = True
        
        else:
            print(f'{self.name} : 시즈모드를 해제합니다.')
            self.damage /= 2
            self.seize_mode = False
        
class Flyalbe:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed
        
    def fly(self, name ,location):
        print(f'{name} : {location} 방향으로 날아갑니다. [속도 {self.fly_speed}]')
        

class FlyableAttackUnit(AttackUnit, Flyalbe):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyalbe.__init__(self, fly_speed)
        
    def move(self, location):
        self.fly(self.name, location)
        
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False
        
    def clocking(self):
        if self.clocked == True:
            print(f'{self.name} : 클로킹 모드 해제합니다')
            self.clocked = False
        
        else:
            print(f'{self.name} : 클로킹 모드로 전환합니다')
            self.clocked = True
            
def game_start():
    print('게임을 시작합니다')
    
def game_over():
    print('Player : gg')
    print('[Player] 님이 게임에서 퇴장하셨습니다.')

# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2개 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 이동
for unit in attack_units:
    unit.move('1시')
    
# 탱크 시즈모드 개발
Tank.seize_delveloped = True
print('탱크 시즈모드 개발이 완료되었습니다.')

# 공격 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    
    elif isinstance(unit, Wraith):
        unit.clocking()

# 공격
for unit in attack_units:
    unit.attack('1시')

# 데미지
for unit in attack_units:
    unit.damaged(randrange(1, 21))

# 게임종료
game_over()