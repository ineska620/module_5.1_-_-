def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
test_function() #функция inner_function успешно вызвана внутри функции test_function.




