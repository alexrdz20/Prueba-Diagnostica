@echo off
cmd /k "echo Verificando GCC... && where gcc >nul 2>&1 && echo [OK] GCC ya esta instalado. || (echo [!] Instalando GCC... && winget install GnuWin32.GCC) && echo. && echo Proceso terminado."
