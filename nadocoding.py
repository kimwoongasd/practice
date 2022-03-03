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
        Flyalbe.__init__(fly_speed)
        
    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)
        
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__('레이스', 80, 20, 5)
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