from crud import add_user, data_of_users, read_db,remove_user_db, delete_user, update_db,create_user, db_params




while True:
    print('menu:')
    print('0 ; zakończ pracę')
    print('1 ; dodaj użytkownika')
    print('2 ; zaktualizuj dane użytkownika')
    print('3 ; usuń użytkownika')
    print('4 ; wyświetl wszystkich użytkowników')

    menu_option: str = input('Podaj opcję do uruchomienia: ')
    if menu_option == '0': break
    if menu_option == '1': create_user(db_params)
    if menu_option == '2': update_db(db_params)
    if menu_option == '3': remove_user_db(db_params)
    if menu_option == '4': read_db(db_params)
