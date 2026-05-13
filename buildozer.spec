[app]

# Título do app
title = Tabuada BGMax

# Nome do pacote (sem espaços, tudo minúsculo)
package.name = tabuadabgmax

# Domínio do pacote
package.domain = br.com.bgmax

# Arquivo principal
source.main = main.py

# Arquivos a incluir no APK
source.include_exts = py,png,jpg,kv,atlas,mp3

# Imagens a incluir
source.include_patterns = *.png, *.mp3

# Versão do app
version = 1.0

# Dependências Python
requirements = python3,kivy==2.2.1,kivymd==1.1.1,gtts,plyer,certifi,urllib3,charset-normalizer,requests

# Orientação da tela
orientation = portrait

# Tela cheia
fullscreen = 0

# Ícone do app (use bg.png ou crie um icon.png 512x512)
#icon.filename = %(source.dir)s/bg.png

# Imagem de splash
#presplash.filename = %(source.dir)s/bgspl.png

# Cor do fundo do splash
android.presplash_color = #000000

# Permissões necessárias
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Versão mínima do Android (5.0)
android.minapi = 21

# SDK alvo
android.api = 33

# NDK version
android.ndk = 25b

# Arquitetura (arm64-v8a para dispositivos modernos, armeabi-v7a para antigos)
android.archs = arm64-v8a, armeabi-v7a

# Aceitar licenças Android automaticamente
android.accept_sdk_license = True

# Modo de debug
android.logcat_filters = *:S python:D

[buildozer]

# Nível de log: 0 = erro, 1 = info, 2 = debug
log_level = 2

# Avisos como erros: desativado
warn_on_root = 1
