import vk


APP_ID = 5672466


def get_user_login():
    return input('Enter login > ')


def get_user_password():
    return input('Enter password > ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        scope='friends',
        user_login=login,
        user_password=password
    )
    api = vk.API(session)
    return sorted(
        api.users.get(user_ids=api.friends.getOnline()),
        key = lambda friend: friend['last_name']
    )


def output_friends_to_console(friends_online):
    print('VK online friends:')
    for (num, friend) in enumerate(friends_online):
        print(num + 1, friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
