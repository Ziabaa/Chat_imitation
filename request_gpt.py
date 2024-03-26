import openai


def check_stop(message):
    stop_words = ["прощавай", "до побачення", "бувай", "до зустрічі", "до скорої зустрічі", "до наступної зустрічі", "до завтра", "до побачення", "відпочивай", "до зустрічі", "успішного дня", "сподіваюся побачити тебе знову", "до скорини", "до нових зустрічей", "всього найкращого", "дякую за звернення", "пока", "гарного дня"]
    lowercase_string = message.lower()
    found = False
    for word in stop_words:
        if word in lowercase_string:
            found = True
            break

    # Перевірка значення found
    if found:
        return True
    else:
        return False


def add_message(messages, role, content):
    messages.append({"role": role, "content": content})


def request_gpt(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message.content

