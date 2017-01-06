@echo off

pip install --upgrade pip wheel setuptools
pip install --upgrade docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew

pip install --upgrade kivy kivy-garden

garden install --app --upgrade filebrowser
