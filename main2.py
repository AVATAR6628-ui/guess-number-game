
import random

print("به بازی حدس اعداد خوش آمدید!")

while True:

    number = random.randint(1, 100)
    chance = 5
    attempt = 0
    win = False

    print("\nمن یک عدد بین 1 تا 100 انتخاب کردم.")
    print("شما 5 فرصت برای حدس زدن دارید.")

    while chance > 0:

        print("\nتلاش", attempt + 1, "از 5")
        print("جان باقی مانده:", chance)

        try:
            guess = int(input("حدس شما: "))

            if guess < 1 or guess > 100:
                print("لطفا عددی بین 1 تا 100 وارد کنید.")
                continue

        except ValueError:
            print("ورودی نامعتبر است! لطفا عدد وارد کنید.")
            continue

        attempt += 1
        chance -= 1

        if guess == number:
            print("\nآفرین! عدد را درست حدس زدی.")
            win = True

            if attempt == 1:
                print("رتبه شما: نمونه ای")
            elif attempt == 2:
                print("رتبه شما: بسیار خوبی")
            elif attempt == 3:
                print("رتبه شما: خوب")
            elif attempt == 4:
                print("رتبه شما: قبول")
            elif attempt == 5:
                print("رتبه شما: با شانس بردی!")

            break

        elif guess > number:
            print("عدد کوچک تری وارد کن.")
        else:
            print("عدد بزرگ تری وارد کن.")

        difference = abs(guess - number)

        if difference <= 5:
            print("خیلی نزدیکی!")
        elif difference <= 15:
            print("نزدیکی، ولی هنوز فاصله داری!")
        else:
            print("خیلی دوری!")

    if win == False:
        print("\nمتاسفانه فرصت های شما تمام شد!")
        print("عدد مخفی برابر بود با:", number)

    # پرسیدن برای بازی مجدد
    while True:

        again = input("\nآیا می خواهی دوباره بازی کنی؟ (بله/خیر): ")

        if again == "بله":
            break

        elif again == "خیر":
            print("\nممنون که بازی کردی. خداحافظ!")
            break

        else:
            print("ورودی نامعتبر است! لطفا فقط بله یا خیر وارد کنید.")

    if again == "خیر":
        break
