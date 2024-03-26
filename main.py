from request_gpt import *
from text_2_speech import *
from graphic import *
prompt_operator = """You are an operator of a Триолан company. Your task is to communicate with me and find out where I have seen Триолан advertisements. Stick to this dialog structure, have a conversation with me, and do not ask me more than 1 question per 1 message:
        use sentences like this to communicate:
        "Вітаю, це компанія Тріолан, чи можете прийняти учать в опитуванні, це займе одну хвилинку."
        "Доброго дня! Вас вітає Тріолан. Маємо для вас невеличке опитування. По часу займе менше хвилини. Візьмете участь?"
        "Чи бачили ви рекламу Тріолан за останні декілька тижнів?"
        "Яку рекламу  про Тріолан Ви бачили за останні 2-3 тижні?"
        "Можливо, щось бачили на вулиці, чи в будинку, чи в інтернеті."
        "Дякую за виділений час, Гарного дня!"
         Write short and to the point, only Ukrainian. Write short and to the point, only Ukrainian."""
prompt_client = "You are a client of the company 'Triolan'. Communicate in Ukrainian, messages should be short and answer questions."

flag = False
operator = True

with open('config.json') as user_file:
    config = json.load(user_file)
openai.api_key = config["openai"]
messages = []
messages_operator = [{"role": "system", "content": prompt_operator}]
messages_client = [{"role": "system", "content": prompt_client}]
count = 0
while count < 5:
    if operator:
        answer = request_gpt(messages_operator)
        if answer.strip():  # Проверка на пустую строку
            messages.append("Operator: " + answer)
            print("Operator: " + answer)

            add_message(messages_operator, "assistant", answer)
            add_message(messages_client, "user", answer)

            file_operator = "operator" + str(count) + ".mp3"
            result = text_to_speech(answer, file_operator)
            if result:
                operator = False
        else:
            print("Получен пустой ответ от оператора.")

    else:
        answer = request_gpt(messages_client)
        if answer.strip():  # Проверка на пустую строку
            messages.append("Client: " + answer)
            print("Client: " + answer)
            add_message(messages_operator, "user", answer)
            add_message(messages_client, "assistant", answer)

            file_client = "client" + str(count) + ".mp3"
            result = text_to_speech(answer, file_client, "FEMALE")
            if result:
                if check_stop(answer):
                    break
                operator = True
                count += 1
        else:
            print("Получен пустой ответ от клиента.")

# Создаем экземпляр класса Tk
root = tk.Tk()

# Устанавливаем размеры окна
root.geometry("700x500")

# Создание кнопок и меток с сообщениями
create_buttons_and_labels(messages, root)

root.mainloop()

