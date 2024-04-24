def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return (length + width) * 2

    if type(length) != int or type(width) != int:
        return f'Enter valid values!'

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle('2', 10))