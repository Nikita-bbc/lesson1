def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
inner_function() #функция не вызывется, потому что содержится в другом пространстве имён