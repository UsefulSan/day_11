import json
from random import shuffle


class Question:
    """
    Содержится информация о вопросе, сложности и ответе
    """

    def __init__(self, question: str, difficulty: str, answer: str) -> None:
        self.question = question
        self.difficulty = difficulty
        self.answer = answer
        self.user_answer = None

    def get_points(self) -> int:
        """Возвращает int, количество баллов.
    Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
    """
        return int(self.difficulty) * 10

    def is_correct(self) -> bool:
        """Возвращает True, если ответ пользователя совпадает
    с верным ответов иначе False.
    """
        return self.answer == self.user_answer

    def build_question(self) -> None:
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        print(f'Вопрос: {self.question}\nСложность {self.difficulty}/5')

    def build_feedback(self) -> bool:
        """
        Отвечает пользователю верный или неверный ответ
        """
        if self.is_correct():
            print(f'Ответ верный, получите {self.get_points()} баллов')
            return True
        print(f'Ответ неверный, верный ответ {self.answer}')
        return False


def read_file() -> list:
    """
    Читает json файл и возвращает список вопросов
    :return: список вопросов
    """
    with open('qda.json', encoding='utf-8') as file:
        contents = json.load(file)
    question_list = []
    for i in contents:
        question_list.append(Question(i['q'], i['d'], i['a']))
    return question_list


def main() -> None:
    points = 0
    count = 0
    print('Игра начинается!')
    question_list = read_file()
    shuffle(question_list)
    for question in question_list:
        question.build_question()
        question.user_answer = input()
        if question.build_feedback():
            points += question.get_points()
            count += 1
        print()
    print(f'Вот и всё!\nОтвечено {count} вопроса из {len(question_list)}\nНабрано {points}')


if __name__ == '__main__':
    main()
