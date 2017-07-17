# -*- coding: cp1251 -*-
import vk_api
   
def main():
    login, password = 'логин', 'пароль'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    wall = vk.wall.get(count=10)['items'] # где count, нужно указать кол-во удаляемых записей(макс.100)
    for x in wall:
        vk.wall.delete(owner_id=402825767, post_id=x['id']) # где owner_id  id очищаемой страницы
if __name__ == '__main__':
    main()
