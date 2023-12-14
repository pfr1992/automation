@echo off

echo.
echo Data e Hora inicio: %DATE% %TIME%
set start_time=%TIME%
echo.

python script02.py

for /l %%i in (1, 1, 1000000) do (
   if %errorlevel% equ 1 (     
        del /f "C:\WhateverFolder\Default\Preferences"
        echo Executando o Comando %%i
        python script02.py
    )
)

echo.
echo Data e Hora fim: %DATE% %TIME%
echo.