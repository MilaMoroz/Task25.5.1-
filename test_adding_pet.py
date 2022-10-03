# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_adding_pet.py


# тестирование добавления животного с фото
def test_adding_of_pet_with_photo(selenium):
    # авторизация
    page = AuthPage(selenium)
    page.enter_email("kryuchkova96@yandex.ru")
    page.enter_password("moroz05092019")
    page.click_btn()

    # создаем объект класса страницы со всеми животными пользователя
    p = AddingPetPage(selenium)
    # вводим данные
    p.add_photo_send(
        r"C:\Users\kryuc\Dexktop\1121529.jpg")
    p.name_field_send('Хатико')
    p.animal_type_field_send('Акита Ину')
    p.age_field_send('5')

    # отправляем данные
    p.submit_btn_click()
    # переходим к списку своих животных
    p.driver.get('https://petfriends.skillfactory.ru/my_pets')
