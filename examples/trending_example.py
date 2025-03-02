from TikTokApi import TikTokApi
import asyncio
import os
import json

with open('secrets/secrets.json') as f:
    secrets = json.load(f)

ms_token = secrets.get("ms_token", None)  # set your own ms_token


async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"), headless=False)
        async for video in api.trending.videos(count=30):
            print(video)
            print(video.as_dict)


if __name__ == "__main__":
    asyncio.run(trending_videos())
