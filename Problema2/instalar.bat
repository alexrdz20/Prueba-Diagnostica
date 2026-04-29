@echo off
cmd /k "echo Verificando Python... && where python >nul 2>&1 && echo [OK] Python ya esta instalado. || (echo [!] Instalando Python... && winget install Python.Python.3) && echo. && echo Proceso terminado."
