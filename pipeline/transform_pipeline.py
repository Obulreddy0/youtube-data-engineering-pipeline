from transform.bronze_to_silver import BronzeToSilverTransformer


class TransformPipeline:

    def run(self):

        print("=" * 60)
        print("STARTING TRANSFORM PIPELINE")
        print("=" * 60)

        transformer = BronzeToSilverTransformer()

        transformer.transform_channel()

        transformer.transform_videos()

        transformer.transform_statistics()

        print("\nTRANSFORM PIPELINE COMPLETED\n")