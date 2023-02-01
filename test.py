def my_shiny_new_decorator(function_to_decorate):
    # def x():
    #     function_to_decorate()
    #     function_to_decorate()
    # return x

    # return function_to_decorate(), print(2)

    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate()
        print("А я - код, срабатывающий после")
    return the_wrapper_around_the_original_function

def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")
# stand_alone_function()



stand_alone_function = my_shiny_new_decorator(stand_alone_function)
stand_alone_function()

# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()



if __name__ == '__main__':
    print('page test <<<')