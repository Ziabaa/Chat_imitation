import json
import requests
import time


def save_audio_file(file_path, audio_data):
    try:
        # Открываем файл для записи
        with open(file_path, 'wb') as file:
            # Записываем аудио данные в файл
            file.write(audio_data)

        print(f"Аудиофайл успешно сохранен: {file_path}")
        return True
    except Exception as e:
        print(f"Не удалось сохранить аудиофайл по пути: {file_path}")
        print(f"Ошибка: {e}")
        return False


def text_to_speech(text, file, voice="", max_retries=2, retry_delay=3):
    headers = {
        "Authorization": "Bearer key"
    }
    url = "https://api.edenai.run/v2/audio/text_to_speech"

    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "providers": "microsoft",
        "language": "uk",
        "text": text,
        "option": voice
    }

    for attempt in range(max_retries):
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:  # Проверка успешного статуса ответа
            result = json.loads(response.text)
            microsoft_data = result.get('microsoft')

            if microsoft_data and 'audio_resource_url' in microsoft_data:
                audio_url = microsoft_data.get('audio_resource_url')
                r = requests.get(audio_url)

                if r.status_code == 200:  # Проверка успешного статуса ответа
                    audio_data = r.content
                    if save_audio_file(file, audio_data):
                        return True

        time.sleep(retry_delay)  # Подождать перед повторной попыткой запроса

    print(f"Не удалось получить аудиофайл для текста: {text}")
    return False