import argparse

from service import Service
from date_time_util import check_date_format

def main():
    parser = argparse.ArgumentParser()
    # 1 create table, 2 add user, 3 select all users 4 generate users, 5 select user
    parser.add_argument("--mode", type=int, choices=[1, 2, 3, 4, 5], 
                        help='1 create table, 2 add user, 3 select all users 4 generate users, 5 select user')
    parser.add_argument("--full_name", type=str, help='"Фамилия Имя Отчество"') # 'Фамилия Имя Отчество'
    parser.add_argument("--birth_date", type=str, help='format yyyy-mm-dd') # format yyyy-mm-dd
    parser.add_argument("--gender", type=str, choices=['Male', 'Female'], help='Male or Female') # Male or Female
    args = parser.parse_args()

    if args.mode not in [1, 2, 3, 4, 5]:
        raise Exception("mode should be in [1, 2, 3, 4, 5] value")    

    service = Service()

    if args.mode == 1:
        service.initialise()
    elif args.mode == 2:
        if args.full_name is None or args.birth_date is None or args.gender is None:
            raise Exception("for mode 1 full_name, birth_date and values should be specified")
        elif args.gender not in ['Male', 'Female']:
            raise Exception("gender should be in ['Male', 'Female'] value")
        elif not check_date_format(args.birth_date):
            raise Exception("birth_date should be in yyyy-mm-dd format")
        
        service.insert_user(args.full_name, args.birth_date, args.gender)
    elif args.mode == 3:
        users = service.select_all_users()
        [print(user) for user in users]
    elif args.mode == 4:
        service.generate_users(1000000)
    else:
        users = service.select_users('F', 'M')



if __name__ == "__main__":
    main()

