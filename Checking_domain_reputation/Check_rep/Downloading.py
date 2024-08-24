import asyncio
import aiohttp
import re
import pandas as pd

async def download_content(url, save_path):
  try:
    async with aiohttp.ClientSession() as session:
      async with session.get(url) as response:
        if response.status == 200:
          content = await response.read()
          with open(save_path, 'wb') as f:
            f.write(content)
          print(f"Content downloaded successfully and saved at: {save_path}")
        else:
          print(
              f"Failed to download content from {url}. Status code: {response.status}"
          )
  except aiohttp.ClientError as e:
    print(f"An error occurred while downloading content from {url}: {e}")


async def load_url(file_path):
  url_list = []
  with open(file_path, 'r') as f:
    for line in f:
      url_list.append(line.strip())
  return url_list


async def main():
  tasks = []
  # Define URLs and save paths
  urls = []
  file_path = 'D:\\Jupyter notebooks\\lists.txt'
  urls = await load_url(file_path)
  save_paths = [f"D:\\Jupyter notebooks\\Check_rep\\list{i}.txt" for i in range(1, 19)]
  # Start asynchronous downloads
  for url, save_path in zip(urls, save_paths):
    tasks.append(asyncio.create_task(download_content(url, save_path)))

  # Wait for all downloads to complete
  await asyncio.gather(*tasks)

if __name__ == "__main__":
  asyncio.run(main())


