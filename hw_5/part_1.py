import aiohttp
import asyncio
import os


async def download_image(session, url, folder):
    async with session.get(url) as response:
        if response.status == 200:
            filename = os.path.join(folder, f'image_{os.path.basename(url)}.jpg')
            with open(filename, 'wb') as f:
                f.write(await response.read())
            print(f'Downloaded {url}')
        else:
            print(f'Failed to download {url}')


async def download_images(num_images, folder):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_images):
            url = 'https://picsum.photos/200/300'
            task = asyncio.create_task(download_image(session, url, folder))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    num_images = int(input("Enter the number of images to download: "))
    folder = input("Enter the folder to save images to: ")

    if not os.path.exists(folder):
        os.makedirs(folder)

    asyncio.run(download_images(num_images, folder))
