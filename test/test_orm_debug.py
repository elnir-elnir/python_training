# #------------------------------------------------------------------------------
# # qa:
# # description: Отладка получения списка групп фикстурой ORM
# #------------------------------------------------------------------------------
#
# # Со стандартной установкой PonyORM (pip install pony) (PonyORM Version: 0.7.19, Python 3.14.5) выполнение
# #  check_db_connection.py завершалось ошибкой:
# # C:\Users\nemo\developing\PythonProject\python_training\env\Scripts\python.exe C:\Users\nemo\developing\PythonProject\python_training\check_db_connection.py
# # Traceback (most recent call last):
# #   File "C:\Users\nemo\developing\PythonProject\python_training\check_db_connection.py", line 68, in <module>
# #     l = db.get_group_list()
# #   File "<string>", line 2, in get_group_list
# #   File "C:\Users\nemo\developing\PythonProject\python_training\env\Lib\site-packages\pony\orm\core.py", line 519, in new_func
# #     result = func(*args, **kwargs)
# #   File "C:\Users\nemo\developing\PythonProject\python_training\fixture\orm.py", line 83, in get_group_list
# #     return list(select(g for g in ORMFixture.ORMGroup))
# #                 ~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# #   File "C:\Users\nemo\developing\PythonProject\python_training\env\Lib\site-packages\pony\orm\core.py", line 5560, in select
# #     return make_query(args, frame_depth=cut_traceback_depth+1)
# #   File "C:\Users\nemo\developing\PythonProject\python_training\env\Lib\site-packages\pony\orm\core.py", line 5546, in make_query
# #     tree, external_names, cells = decompile(gen)
# #                                   ~~~~~~~~~^^^^^
# #   File "C:\Users\nemo\developing\PythonProject\python_training\env\Lib\site-packages\pony\orm\decompiling.py", line 43, in decompile
# #     decompiler = Decompiler(codeobject)
# #   File "C:\Users\nemo\developing\PythonProject\python_training\env\Lib\site-packages\pony\orm\decompiling.py", line 160, in __init__
# #     decompiler.get_instructions()
# #     ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
# #   File "C:\Users\nemo\developing\PythonProject\python_training\env\Lib\site-packages\pony\orm\decompiling.py", line 220, in get_instructions
# #     arg = [code.co_varnames[oparg]]
# #            ~~~~~~~~~~~~~~~~^^^^^^^
# # IndexError: tuple index out of range
# #
# # Process finished with exit code 1
# #
# #
# #
# # Для решения ошибки установка экспериментального патча pip install pony --upgrade --pre не помогла.
# # В итоге удалила стандартную версию PonyORM и установила форк:
# # pip uninstall pony
# # pip install git+https://github.com/j4hangir/pony.git
# # Не стала понижать версию Python до 3.10 или 3.11
# #
# #
# #
# # РЕЗУЛЬТАТ: При выполнении кода из данного файла как Python-скрипта список групп выводится
#
# # Затем вернула официальную версию PonyORM 0.7.19 - все работает (странно...)
#
#
# import logging
#
# # Настройка логирования
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
#
# from pony.orm import sql_debug, db_session
# sql_debug(True)
#
# from fixture.orm import ORMFixture
#
# print("=== НАЧАЛО ТЕСТА ===\n")
#
# # Подключаемся к БД
# print("1. Подключение к БД...")
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# print("Подключено!\n")
#
# # Получаем группы
# print("2. Получение списка групп...")
# groups = db.get_group_list()
# print(f"Найдено групп: {len(groups)}")
#
# print("\n3. Вывод групп:")
# for group in groups:
#     print(f"  {group.id}: {group.name}")
#
# print("\n=== КОНЕЦ ТЕСТА ===")