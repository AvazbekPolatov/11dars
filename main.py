import aiohttp
import asyncio
from colorama import Fore, Style, init
import time

init(autoreset=True)

api_key = "fc8df63e5d07e69eea924489139ab4dd"  

# 1. Paroldagi raqamlarni olib tashlash
async def remove_digits_from_password(password):
    result = "".join([char for char in password if not char.isdigit()])
    print(f"{Fore.GREEN}Yangilangan parol: {Fore.CYAN}{result}")

# 2. Matnning birinchi 10 belgisini chiqarish
async def first_ten_characters(text):
    result = text[:10]
    print(f"{Fore.YELLOW}Birinchi 10 belgisi: {Fore.CYAN}{result}")

# 3. Ismdagi raqamlarni olib tashlash
async def clean_name(name):
    result = "".join([char for char in name if not char.isdigit()])
    print(f"{Fore.MAGENTA}Tozalangan ism: {Fore.CYAN}{result}")

# 4. Matndagi katta harflarni kichik qilib va bo'sh joylarni olib tashlash
async def process_text(text):
    result = "".join([char.lower() for char in text if not char.isspace()])
    print(f"{Fore.GREEN}Qayta ishlangan matn: {Fore.CYAN}{result}")

# 5. Faqat unli harflarni chiqarish
async def extract_vowels(text):
    vowels = "aeiouAEIOU"
    result = "".join([char for char in text if char in vowels])
    print(f"{Fore.BLUE}Unli harflar: {Fore.CYAN}{result}")

# 6. "a" va "b" ni "#" ga o'zgartirish
async def replace_ab_with_hash(word):
    result = word.replace("ab", "#")
    print(f"{Fore.YELLOW}O'zgartirilgan so'z: {Fore.CYAN}{result}")

# 7. Matnni teskari chiqarish
async def reverse_numeric_text(text):
    if text.isdigit():
        result = text[::-1]
        print(f"{Fore.GREEN}Teskari matn: {Fore.CYAN}{result}")
    else:
        print(f"{Fore.RED}Matn faqat raqamlardan iborat emas!")

# 8. O'rtadagi harfni olib tashlash
async def remove_middle_character(word):
    middle = len(word) // 2
    result = word[:middle] + word[middle+1:]
    print(f"{Fore.MAGENTA}O'rtadagi harfi olib tashlangan so'z: {Fore.CYAN}{result}")

# 9. "a" harfi bilan tugasa, kichik harfga o'zgartirish
async def lowercase_if_ends_with_a(name):
    if name.endswith("a"):
        print(f"{Fore.GREEN}Kichik harfga o'zgartirildi: {Fore.CYAN}{name.lower()}")
    else:
        print(f"{Fore.RED}Ism o'zgartirilmadi: {Fore.CYAN}{name}")

# 10. Takrorlanmaydigan harflarni chiqarish
async def remove_duplicates(text):
    seen = set()
    result = "".join([char for char in text if char not in seen and (seen.add(char) or True)])
    print(f"{Fore.YELLOW}Takrorlanmaydigan harflar: {Fore.CYAN}{result}")

# 11. Faqat unli harflardan iborat so'zni katta harflarga o'zgartirish
async def uppercase_if_vowels_only(word):
    vowels = "aeiouAEIOU"
    if all(char in vowels for char in word):
        print(f"{Fore.BLUE}Katta harflarda: {Fore.CYAN}{word.upper()}")
    else:
        print(f"{Fore.RED}So'z faqat unli harflardan iborat emas: {Fore.CYAN}{word}")

# 12. OpenWeatherMap API orqali ob-havo ma'lumotlari
async def get_weather(city):
    city = city.strip()  # Shahar nomidagi bo'sh joylarni olib tashlash
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print(
                    f"{Fore.GREEN}Hozir {city} shahrida havo harorati: {data['main']['temp']} gradus. "
                    f"{Fore.BLUE}Havo: {data['weather'][0]['description'].capitalize()}."
                )
            else:
                print(f"{Fore.RED}Shahar nomi noto'g'ri kiritildi!!!")


# Asinxron kodni ishga tushirish
async def main():
    print(f"{Fore.CYAN}{'-'*40}")
    start_time = time.time()
    while True:
        city = input(f"{Fore.YELLOW}Shahar nomini kiriting: {Style.RESET_ALL}")
        if city.lower() == "stop":
            print(f"{Fore.RED}Dastur to'xtadi!!!")
            elapsed_time = time.time() - start_time
            print(f"{Fore.MAGENTA}{elapsed_time:.3f} sekund davomida ishladi!!!")
            break
        await get_weather(city)
        print(f"{Fore.CYAN}{'-'*40}")

async def main():
    await remove_digits_from_password("pass1234")
    await first_ten_characters("Hello, this is a test!")
    await clean_name("John123")
    await process_text("  THIS IS A test   ")
    await extract_vowels("Beautiful World!")
    await replace_ab_with_hash("table")
    await reverse_numeric_text("15642")
    await remove_middle_character("testing")
    await lowercase_if_ends_with_a("Anna")
    await remove_duplicates("abacadef")
    await uppercase_if_vowels_only("aei")
    await get_weather("Tashkent")



# Asinxron kodni ishga tushirish
if __name__ == "__main__":
    asyncio.run(main())
