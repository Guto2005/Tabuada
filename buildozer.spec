[app]
title = Tabuada com Audio
package.name = tabuada
package.domain = br.com.bgmax

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0,gtts,plyer,certifi,requests,charset-normalizer,idna,urllib3

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.ndk_api = 21

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
