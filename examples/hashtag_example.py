from TikTokApi import TikTokApi
import asyncio
import os
import csv
import json

with open('secrets/secrets.json') as f:
    secrets = json.load(f)

ms_token = secrets.get("ms_token", None)  # set your own ms_token


async def get_hashtag_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"), headless=False)
        hashtag = "makeup"
        video_count = 1000
        tag = api.hashtag(name=hashtag)
        async for video in tag.videos(count=video_count):
            # print(video)
            # Convert video to dictionary
            video_dict = video.as_dict

            # Write to CSV file
            with open(f'data/videos_{hashtag}_{video_count}.csv', mode='a', newline='') as csv_file:
                fieldnames = video_dict.keys()
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                if csv_file.tell() == 0:
                    writer.writeheader()
                writer.writerow(video_dict)

        print(f"stored video for hashtag {hashtag} with total rows {video_count}")


if __name__ == "__main__":
    asyncio.run(get_hashtag_videos())
