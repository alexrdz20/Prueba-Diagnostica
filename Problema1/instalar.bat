@echo off
echo ==================================================
echo VERIFICANDO PYTHON...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Instalando Python...
    winget install Python.Python.3 --silent
) else (
    echo [OK] Python ya esta instalado.
)

echo.
echo ==================================================
echo VERIFICANDO JAVA...
where javac >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Instalando Java...
    winget install Oracle.JDK.21 --silent
) else (
    echo [OK] Java ya esta instalado.
)

echo.
echo ==================================================
echo Proceso finalizado.
echo ==================================================
pause
