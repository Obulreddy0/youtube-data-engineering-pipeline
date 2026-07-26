from extractors.channel_extractor import ChannelExtractor


def main():

    extractor = ChannelExtractor()

    channel = extractor.get_channel_details()

    print("\n✅ Channel Extracted Successfully\n")

    print(
        f"Channel Name : "
        f"{channel['snippet']['title']}"
    )

    print(
        f"Subscribers : "
        f"{channel['statistics'].get('subscriberCount')}"
    )

    print(
        f"Videos : "
        f"{channel['statistics'].get('videoCount')}"
    )

    print(
        f"Views : "
        f"{channel['statistics'].get('viewCount')}"
    )


if __name__ == "__main__":
    main()