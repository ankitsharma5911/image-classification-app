[app]
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,tflite # add tflite if needed
version = 0.1
requirements = python3,kivy,opencv-python,tensorflow
orientation = portrait
fullscreen = 0

[android]
permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.numeric_version = 1

[buildozer]
log_level = 2