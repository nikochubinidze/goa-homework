2) გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი
sum = 1
for i in range (1,12):
  sum = i 
  print(sum)

3) გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი
i = 1 
sum = 1

while i < 11:
    i += 1
    sum= i
    print(sum)


4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:       10 % 2 = 0;        5 % 2 = 1)
user_number = int(input("Enter your number:"))

if user_number % 2 == 0:
    print("Luwia")
else:
    print("Kentia")

5) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade
ამ ფოტოს მიხედვით: (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ
"Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)
user_num = int(input("Enter your num:"))

for i in range(90,101):
    if user_num == i:
        print("Grade A")


for i in range(80, 90 ):
    if user_num == i:
        print("Grade B")