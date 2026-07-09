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
