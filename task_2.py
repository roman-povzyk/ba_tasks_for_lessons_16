def stop_words(words):
    def wrapper(*args, **kwargs):
        result = words(*args, **kwargs)
        return result
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    slogan = "drinks pepsi in his brand new BMW!"
    slogan_list = slogan.split(" ")
    for stop_word in stop_words:
        for i in slogan_list:
            if stop_word == slogan_list[i]:
                slogan_list[i] = "*"
    slogan_join = slogan_list.join
    return f"{name} {slogan_join}"


print(create_slogan("Steve"))