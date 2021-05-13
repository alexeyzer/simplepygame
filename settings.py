class Settings():
    def __init__(self):
        #настройка главного окна
        self.bg_color = (230, 230, 230)
        self.screen_width = 1200
        self.screen_height = 750
        #настройка скорости перемещения и тд
        self.player_hp = 15
        self.player_acc = 0.1
        #параметры пули
        self.bullet_speed = 6
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60

        self.background_speed = 4
        self.decorations_speed = 6
