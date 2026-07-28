from transform.silver_to_gold import SilverToGoldTransformer


class GoldPipeline:

    def run(self):

        print("=" * 60)
        print("STARTING GOLD PIPELINE")
        print("=" * 60)

        transformer = SilverToGoldTransformer()

        transformer.transform()

        print("=" * 60)
        print("GOLD PIPELINE COMPLETED")
        print("=" * 60)