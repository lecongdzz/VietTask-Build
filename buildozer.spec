[app]
title = TTBoost Automation VIP
package.name = viettasktool
package.domain = com.ttboost
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Thư viện yêu cầu
requirements = python3,kivy

orientation = portrait
fullscreen = 1

# Cấu hình Android chuẩn để không bị crash trên server
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a
android.allow_backup = True

# Các quyền cơ bản nếu sau này ông làm tool MMO cần kết nối mạng
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
