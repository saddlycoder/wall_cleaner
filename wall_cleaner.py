# -*- coding: cp1251 -*-
import vk_api
   
def main():
    login, password = '�����', '������'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    try:
        wall = vk.wall.get(count=10)['items'] # ��� count, ����� ������� ���-�� ��������� �������(����.100)
	except vk_api.VkApiError as err:
	    print(err)
		return
    for(x in wall):
        vk.wall.delete(owner_id=402825767, post_id=x['id']) # ��� owner_id  id ��������� ��������
if __name__ == '__main__':
    main()
