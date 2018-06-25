thang_truoc,thang_sau = map(int, input().split())

gio_dien = thang_sau - thang_truoc
tong_tien = 0
bang_gia =[1484,1533,1786,2242,2503,2587]
if gio_dien<= 50:
    tong_tien = gio_dien* bang_gia[0]
elif gio_dien <=100:
    tong_tien = 50*bang_gia[0] + (gio_dien-50)*bang_gia[1]
elif gio_dien <= 200:
    tong_tien = 50 *bang_gia[0] + 50*bang_gia[1] +(gio_dien-100)*bang_gia[2]
elif gio_dien <=300:
    tong_tien = 50 * bang_gia[0] + 50 * bang_gia[1] + 100 * bang_gia[2] + (gio_dien-200)* bang_gia[3]
elif gio_dien <=400:
    tong_tien = 50 * bang_gia[0] + 50 * bang_gia[1] + 100 * bang_gia[2] + 100 * bang_gia[3] + (gio_dien- 300)* bang_gia[4]
else:
    tong_tien = 50 * bang_gia[0] + 50 * bang_gia[1] + 100 * bang_gia[2] + 100 * bang_gia[3] + 100 * bang_gia[4] +(gio_dien -400)*bang_gia[5]

print(tong_tien*110/100)
