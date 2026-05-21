import sys
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class VietTaskLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(VietTaskLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        
        # Ép nền đen Cyberpunk cho app
        Window.clearcolor = get_color_from_hex('#0A0A0C')
        
        # Tiêu đề Tool chuyên nghiệp
        self.title_label = Label(
            text='[b]VIETTASK AUTOMATION VIP[/b]', 
            markup=True, 
            font_size='24sp',
            color=get_color_from_hex('#00FF66'), # Xanh neon rực rỡ
            size_hint_y=None,
            height=50
        )
        self.add_widget(self.title_label)
        
        # Thông tin bản quyền thương hiệu Lê Công
        self.credits_label = Label(
            text='[i]Admin: Lê Công - Co-Developer: Quyền Béo[/i]',
            markup=True,
            font_size='14sp',
            color=get_color_from_hex('#00E5FF'), # Xanh cyan công nghệ
            size_hint_y=None,
            height=30
        )
        self.add_widget(self.credits_label)
        
        # Khung log hiển thị trạng thái giả lập giống Termux
        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.log_label = Label(
            text='[b][Khởi động][/b] Hệ thống đã sẵn sàng...\n[b][Hệ thống][/b] Đang chờ cấu hình tác vụ...',
            markup=True,
            font_size='14sp',
            color=get_color_from_hex('#FFFFFF'),
            halign='left',
            valign='top',
            size_hint_y=None
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)
        
        # Nút bấm chính để test tương tác UI
        self.start_btn = Button(
            text='KÍCH HOẠT HỆ THỐNG',
            font_size='18sp',
            bold=True,
            background_normal='',
            background_color=get_color_from_hex('#FF007F'), # Hồng neon cực chiến
            color=get_color_from_hex('#FFFFFF'),
            size_hint_y=None,
            height=60
        )
        self.start_btn.bind(on_press=self.on_start_click)
        self.add_widget(self.start_btn)
        
    def on_start_click(self, instance):
        self.log_label.text += '\n[b][Chạy][/b] Đang kiểm tra cấu hình tài khoản...'
        self.log_label.text += '\n[b][Thông báo][/b] Môi trường UI hoạt động mượt mà!'

class VietTaskApp(App):
    def build(self):
        self.title = 'TTBoost Automation VIP'
        return VietTaskLayout()

if __name__ == '__main__':
    VietTaskApp().run()
      
