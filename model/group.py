#------------------------------------------------------------------------------
# qa:
# description:
#------------------------------------------------------------------------------

class Group:
    # method parameters change for default (lesson 3-2)
    # def __init__(self, name, header, footer):

    # None is special value/ None means that field not initialized (lesson 3-2)
    # Добавляем в параметры идентификатор (урок 4-7)
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id


    # Для получения информации об объекте реализуем функцию, которая определяет вывод объекта в консоль
    # урок 4-8
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)


    # Определяем функцию для логического сравнения, т. е. по смыслу (по именам, идентификаторам).
    # Без это функции сравнение идет по ссылкам на расположение в памяти (по физическому
    # расположению объектов, в результате чего 2 объекта с одинаковыми именами и идентификаторами
    # считаются разными объектами (урок 4-8)
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
