###CAPSTONE PROJECT PURWADHIKA MODUL 1

#Program CRUD sederhana
#Data Karyawan

karyawan = [{
    'Nama' : 'Sujiwo',
    'Umur' : 30,
    'Salary' : 1500000,
    'Alamat' : 'Rancamekar',
    'Status': 'Fulltime'},
    {'Nama' : 'Dadang',
    'Umur' : 40,
    'Salary' : 7000000,
    'Alamat' : 'Tegallega',
    'Status' : 'Magang'},
    {'Nama': 'Priambodo',
    'Umur' : 35,
    'Salary' : 5000000,
    'Alamat' : 'Dago Giri',
    'Status' : 'Fulltime'},
    {'Nama' : 'Rahman',
    'Umur' : 23,
    'Salary': 46000000,
    'Alamat' : 'Dago Atas',
    'Status' : 'Magang'},
    {'Nama' : 'Namira',
    'Umur' : 23,
    'Salary' : 34000000,
    'Alamat': 'Sukaasih',
    'Status' : 'Fullime'}
]

##Functions 

def Tabel():
    print('NIP\t| Nama\t\t| Umur\t| Salary\t | Alamat  \t | Status')
    for i in range(len(karyawan)):
        print('{}\t| {} \t| {}\t| {}\t | {}\t | {}\t'.format(i, karyawan[i]['Nama'], karyawan[i]['Umur'], karyawan[i]['Salary'], karyawan[i]['Alamat'], karyawan[i]['Status']))
        continue

def TabelTertentu(key):
    if(key in range(len(karyawan))):
        print('NIP\t| Nama\t\t| Umur\t| Salary\t | Alamat \t | Status')
        print('{}\t| {}\t| {}\t| {}\t | {} \t  | {}\t '.format(key, karyawan[key]['Nama'], karyawan[key]['Umur'], karyawan[key]['Salary'], karyawan[key]['Alamat'], karyawan[key]['Status']))

#Opsi pertama
def MenampilkanData():
    while(True):
        print('''
        ___________________________________
        Data Karyawan PT. Yudha Bermartabat''')
        menu1 =  input('''
        Masukan pilihan anda:
        1. Data Seluruh Karyawan
        2. Data Karyawan Tertentu
        3. Kembali ke Menu Utama
        Masukan Pilihan anda : ''')

        if(menu1 == '1'):
            print('NIP\t| Nama\t\t| Umur\t| Salary\t | Alamat \t | Status')
            for i in range(len(karyawan)):
                print('{}\t| {}\t| {}\t| {}\t | {}\t | {}\t'.format(i, karyawan[i]['Nama'], karyawan[i]['Umur'], karyawan[i]['Salary'], karyawan[i]['Alamat'], karyawan[i]['Status']))

        elif(menu1 == '2'):
            key = int(input('Masukan Nomor Induk Pegawai : '))
            if(key in range(len(karyawan))):
                print('NIP\t| Nama \t \t| Umur\t| Salary\t | Alamat\t | Status')
                print('{}\t| {}\t| {}\t| {}\t | {}\t | {}\t'.format(key, karyawan[key]['Nama'], karyawan[key]['Umur'], karyawan[key]['Salary'], karyawan[key]['Alamat'], karyawan[key]['Status']))
            else:
                print('Oops!, Data tak ditemukan')
        elif(menu1 == '3'):
            break
        else:
            continue
#Opsi Kedua 'Menambahkan Karyawan'
def MenambahkanKaryawan():
    while(True):
        menu2 = input('''
        Penambah Data
        1. Menambah Data Karyawan
        2. Kembali ke Menu Utama :  ''')
        if(menu2 == '1'):
            Nama = input('Masukan Nama Karyawan yang ingin ditambahkan : ')
            Umur = input('Masukan Usia yang bersangkuran : ')
            Salary = input('Berapa Salary karyawan tersebut : ')
            Alamat = input('Masukan Nama Jalan Tempat Tinggal (Tanpa imbuhan "jalan/jln/jl etc." : ')
            Stat = input('Masukan Status Karyawan (magang/fulltime) : ')
            for key in range(len(karyawan)):
                if karyawan[key]['Nama'].lower() == Nama.lower() and karyawan[key]['Alamat'].lower() == Alamat.lower():
                    print('Data Sudah Ada'.upper())
                    break
                else:
                    submenu2 = input('Simpan Data? (Y/N) : ')
                    if(submenu2.lower() == 'y'):
                        karyawan.append({'Nama' : Nama, 'Umur': Umur, 'Salary' : Salary, 'Alamat': Alamat, 'Status': Stat.capitalize()})
                        print('Data telah ditambahkan')
                        print('Daftar karyawan terupdatenya saat ini')
                        print('NIP\t | Nama\t\t| Umur\t | Salary\t | Alamat\t | Status')
                        for i in range(len(karyawan)):
                            print('{}\t | {}\t| {}\t| {}\t |{}\t | {}\t'.format(i, karyawan[i]['Nama'], karyawan[i]['Umur'], karyawan[i]['Salary'],karyawan[i]['Alamat'], karyawan[i]['Status']))
                        break
                    elif(submenu2.lower() == 'n'):
                        print('Data tidak ditambahkan')
                        break
                    else:
                        print('Tidak Berhasil Menambahkan Data')
                        print('Daftar karyawan terupdatenya Tanpa tambahan data saat ini')
                        print('NIP\t | Nama \t \t | Umur\t | Salary\t | Alamat\t | Status')
                        for i in range(len(karyawan)):
                            print('{}\t | {}\t| {}\t| {}\t |{}\t'.format(i, karyawan[i]['Nama'], karyawan[i]['Umur'], karyawan[i]['Salary'],karyawan[i]['Alamat'], karyawan[i]['Status']))
                        break
        elif(menu2 == '2'):
            break
        else :
            continue

#Opsi ketiga 'Mengurangi Karyawan'
def MengurangiKaryawan():
    while(True):
        menu3 = input('''Fitur Penghapusan Data
        1. Menghapus Data Karyawan
        2. Keluar
        Pilihan Anda : ''')
        if(menu3 == '1'):
            print('Berikut Daftar Karyawan saat ini, Silahkan pilih NIP karyawan yang akan dihapus')
            print('NIP\t | Nama\t \t | Umur\t | Salary\t | Alamat\t| Status')
            for i in range(len(karyawan)):
                print('{}\t | {}\t | {}\t | {}\t | {}\t | {}\t '.format(i, karyawan[i]['Nama'], karyawan[i]['Umur'], karyawan[i]['Salary'],karyawan[i]['Alamat'], karyawan[i]['Status']))
            indexBuah = int(input('Masukan NIP karyawan yang akan diapus ; '))
            if indexBuah not in range(len(karyawan)):
                print('Data tak ditemukan')
                continue
            elif indexBuah in range(len(karyawan)):
                del karyawan[indexBuah]
                print('Data Terhapus')
                break
            else:
                continue
        elif(menu3 == '2'):
            break
        else:
            continue
#Opsi keempat 'Update'
def MengupdateKaryawan():
    while(True):
        menu4 = input('''
        
        fitur update karyawan
        1. Update Karyawan
        2. Kembali ke Menu utama : ''')
        if(menu4 == '1'):
            print(Tabel())
            yangDiupdate = int(input('''Masukan NIP karyawan yang akan di update
            '''))
            key = yangDiupdate
            print(TabelTertentu(key))

            while yangDiupdate in range(len(karyawan)):
                tipeOpsi = input('''Apa yang ingin anda ingin anda update? :
                1. Nama
                2. Umur
                3. Salary
                4. Alamat
                5. Status
                6. Keluar
                Pilihan anda :  ''')
                if (tipeOpsi == '1'):
                    namaBaru = input('Masukan Nama Baru : ')
                    yesno = input('Simpan data? (Y/N) : ')
                    if(yesno.lower() == 'n'):
                        print('Data tidak ditambahkan')
                        break
                    elif(yesno.lower() == 'y'):
                        namaBaru = namaBaru.replace(" ","")
                        karyawan[yangDiupdate]['Nama'] = namaBaru.capitalize()
                        print(Tabel(), '''
                        
                        Data Terupdate''')
                    else:
                        print('Data tidak ditambahkan')
                        continue
                elif(tipeOpsi == '2'):
                    umurBaru = input('Masukan Umur ter-update : ')
                    yesno = input('Simpan Data? (Y/N)')
                    if(yesno.lower() == 'n'):
                        print('Data tidak ditambahkan')
                        break
                    elif(yesno.lower() == 'y'):
                        if int(umurBaru) in range(200):
                            karyawan[yangDiupdate]['Umur'] = int(umurBaru)
                            print('Data terupdate \n' ,Tabel())
                        else :
                            print('masukan umur dengan benar')
                            break
                    else:
                        print('Data tidak ditambahkan')
                        continue
                elif(tipeOpsi == '3'):
                    salaryBaru = input('Masukan Besaran Gaji terbaru : ')
                    yesno = input('Simpan Data ? (Y/N) : ')
                    if(yesno.lower() == 'n'):
                        print('Data tidak ditambahkan')
                        break
                    elif(yesno.lower() == 'y'):
                        karyawan[yangDiupdate]['Salary'] = int(salaryBaru)
                        print(Tabel(), '''
                        Data terupdate ''')
                    else:
                        print('Data tidak ditambahkan')
                        continue
                elif(tipeOpsi == '4'):
                    alamatBaru = input('Masukan alamat tanpa imbuhan "Jalan/Jl./Jln" : ')
                    yesno = input('Simpan Data? (Y/N) : ')
                    if(yesno.lower() == 'n'):
                        print('Data tidak ditambahkan')
                    elif(yesno.lower() == 'y'):
                        karyawan[yangDiupdate]['Alamat'] = alamatBaru
                        print(Tabel(), ''' 
                        Data terupdate''')
                    else:
                        print('Data tidak ditambahkan')
                        continue
                elif(tipeOpsi == '5'):
                    status = input('Masukan status karyawan terbaru (Magang/Fulltime): ')
                    yesno = input('Simpan Data? (Y/N) : ')
                    if(yesno.lower() == 'n'):
                        print('Data tidak ditambahkan')
                    elif(yesno.lower() == 'y'):
                        if(status.lower() == 'magang' or status.lower() == 'fulltime'):
                            karyawan[yangDiupdate]['Status'] = status.capitalize()
                            print(Tabel(), '''
                            Data berhasil terupdate''')
                        else:
                            print('Data tidak ditambahkan')
                            break
                    else:
                        continue
                elif(tipeOpsi == '6'):
                    break
                else:
                    continue
            else:
                print('Karyawan tidak ditemukan \n ')
        elif(menu4 == '2'):
            print('Anda keluar dari opsi Update')
            break



while (True):
    pilihanMenu = input('''
    Selamat Datang di aplikasi karyawan PT.YudhaBermartabat!
    Silahkan masukan opsi yang diinginkan :
    1. Mengakses Data Karyawan
    2. Menambah Karyawan
    3. Menghapus Data Karyawan
    4. Mengubah Data Karyawan
    5. Exit Program 
    Masukan pilihan anda : ''')


    if(pilihanMenu == '1'):
        MenampilkanData()
    elif(pilihanMenu =='2'):
        MenambahkanKaryawan()
    elif(pilihanMenu == '3'):
        MengurangiKaryawan()
    elif(pilihanMenu == '4'):
        MengupdateKaryawan()
    elif(pilihanMenu == '5'):
        print('''
        ______________________________
        Anda sudah keluar dari program
        ______________________________''')
        break
    else:
        print('Pilihan yang anda masukan salah')





        


