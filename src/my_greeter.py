from datetime import datetime

class MyGreeter:
    def greeting(self):
        # 获取当前小时
        now_hour = datetime.now().hour

        # 判断当前小时属于哪个时间段
        if 6 <= now_hour < 12:
            return "Good morning"
        elif 12 <= now_hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"
