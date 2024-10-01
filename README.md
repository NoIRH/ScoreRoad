# ScoreRoad

## Инициализация проекта 
1. В директории в которую был был склонирован репозиторий создаете виртуальную среду 
``` 
    python -m venv .venv
```
  1. Если это делает через powershell то вначале нужно дать разврешение на выполнение сторонних 
    ``` 
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
2. После этого устанавливаем все библиотеки по файлу с зависимостями 
```
    python -m pip install -r requirements.txt.
```
  1. Если же нужно создать или обновить файл с зависимостями то используется следующая команда 
    ```
        pip freeze > requirements.txt
    ```