from transform.bronze_to_silver import BronzeToSilverTransformer


class TransformPipeline:

    def run(self):

        print("=" * 60)
        print("STARTING TRANSFORM PIPELINE")
        print("=" * 60)

        transformer = BronzeToSilverTransformer()

        transformer.transform()

        print("=" * 60)
        print("TRANSFORM PIPELINE COMPLETED")
        print("=" * 60)