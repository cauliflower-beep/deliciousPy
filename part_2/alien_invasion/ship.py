import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):  # ai_game 指向当前AlienInvasion实例的引用
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen  # 方便ship访问AI中定义的所有游戏资源
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # 以处理矩形的形式处理所有游戏元素，因而高效

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船属性x中存储小数值
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据self.x更新rect对象 rect.x 只存储self.x的整数部分
        self.rect.x = self.x
