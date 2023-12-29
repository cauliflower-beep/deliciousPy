import sys
import time

from settings import Settings
from ship import Ship

import pygame


class AlienInvasion:
    """管理游戏资源和行为"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()

        # 设置类作为属性
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            # 每次循环时都重绘屏幕
            self._update_screen()

    """
    辅助方法在类中执行任务，但并非通过实例调用
    python中的辅助方法的名称以单个下划线打头
    """

    def _check_events(self):
        """响应按键和鼠标事件"""
        # 监视键盘和鼠标事件 如果没有获取到事件，不会阻塞
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 向右移动飞船
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    # 向右移动飞船
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # 停止右移
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    # 向右移动飞船
                    self.ship.moving_left = False

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并启动游戏
    ai = AlienInvasion()
    ai.run_game()
