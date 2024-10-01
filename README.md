# ScoreRoad

## Инициализация проекта 
1. В директории в которую был был склонирован репозиторий создаете виртуальную среду 
``` 
    python -m venv .venv
```
   - Если это делает через powershell то вначале нужно дать разрешение на выполнение сторонних скриптов
``` 
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
2. После этого активируем виртуальную среду 
```
    .venv\Scripts\Activate.ps1
```
3. После этого устанавливаем все библиотеки по файлу с зависимостями 
```
    python -m pip install -r requirements.txt.
```
   - Если же нужно создать или обновить файл с зависимостями то используется следующая команда 
```
    pip freeze > requirements.txt
```