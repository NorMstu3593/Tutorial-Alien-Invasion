class Settings:
    """存储游戏中所有设置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5

        # 子弹设置（宽3像素，高15像素，深灰色）
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
