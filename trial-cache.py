import datetime as dt
import time
from tqdm import tqdm
from mini import bar


def get_home_option ():
    Home_option = ('c','e')

    while True:
        bar('Menyiapkan Home_Menu')
        print('***Home_Menu***')
        print('c = Clock In')
        print('e = Exit' )
        print()

        user_input = input('ENTER AN OPTION :')

        if user_input in Home_option:
            return user_input
        
        else :
            print(14*'=')
            print('INPUT INVALID!')
            print(14*'=')

while True:
    user_input = get_home_option()
    if user_input == 'c':
                bar('Menyiapkan waktu')
                ClockIn = dt.datetime.now()
                now_is = dt.datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
                print(now_is)
                
                bar('Preparing clock in')
                print("Selamat!")
                print("Clock In kamu tercatat ")
                print("di tanggal :", dt.date.today())
                print("pada pukul :", dt.datetime.now().strftime("%H:%M:%S") )
                
                def get_tracktime_option ():
                    tracktime_option = ('o', 'b', 'h')

                    while True :
                        bar('Preparing track time menu')
                        print('***Track_Time_Menu***')
                        print('o = Clock Out')
                        print('b = Break')
                        print('h = Home Menu' )
                        print()
                        print('Jika kamu kembali ke home\nProgram ini akan auto clock out..')
                        
                        user_input = input('ENTER AN OPTION :')
                        
                        if user_input in tracktime_option:
                            return user_input   
                        
                        else :
                            print(14*'=')
                            print('INPUT INVALID!')
                            print(14*'=')

                user_input = get_tracktime_option()
                if user_input == 'o':
                    bar('Calculating clock time')
                    ClockOut = dt.datetime.now()
                    user_time_spend = ClockOut - ClockIn
                    print(user_time_spend)
                    
                    bar('Writing time data')
                    print("Clock Out kamu tercatat ")
                    print("di tanggal :", dt.date.today())
                    print("pada pukul :", dt.datetime.now().strftime("%H:%M:%S"), "\n")
                    print("durasi ClockIn kamu adalah:")
                    print(user_time_spend)
                    
                elif user_input == 'b':
                    bar('Preparing break')
                    print('kamu sedang Break!')
                    print('Selamat Istirahat :)')
                    
                    bar('Calculating time')
                    ClockOut = dt.datetime.now()
                    user_time_spend = ClockOut - ClockIn
                    print(user_time_spend)
                    
                    bar('Writing time data')
                    print("Clock Out kamu tercatat ")
                    print("di tanggal :", dt.date.today())
                    print("pada pukul :", dt.datetime.now().strftime("%H:%M:%S"), "\n")
                    print("durasi ClockIn kamu adalah:")
                    print(user_time_spend)
                    
                elif user_input == 'h':
                    bar('Calculating time')
                    ClockOut = dt.datetime.now()
                    user_time_spend = ClockOut - ClockIn
                    print(user_time_spend)
                    
                    bar('Writting data')
                    print("Clock Out kamu tercatat ")
                    print("di tanggal :", dt.date.today())
                    print("pada pukul :", dt.datetime.now().strftime("%H:%M:%S"), "\n")
                    print("durasi ClockIn kamu adalah:")
                    print(user_time_spend)
                        
    elif user_input == 'e':
                bar('Cleaning the program')
                print('See you soon! =)')
                print('program end!')
                print()
                exit()