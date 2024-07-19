import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from aiogram import Bot, Dispatcher, types, filters
import asyncio
from pytube import YouTube
from aiogram.types import InputFile


bot = Bot(token='7351668791:AAFEtTi51nu8iC1ETgGAE5ArzR0PSTRLOTs')
dp = Dispatcher(bot=bot)


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Welcome to youtube downloader bot, send your video's link and i will download it for you")


@dp.message()
async def download_function(message: types.Message):
    url = YouTube(message.text)
    video = url.streams.get_highest_resolution()
    result = video.download()
    with open(result, "rb") as video_file:
        await message.answer_video(video=video_file)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
