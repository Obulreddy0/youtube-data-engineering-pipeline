from pipeline.extract_pipeline import ExtractPipeline
from pipeline.transform_pipeline import TransformPipeline
from pipeline.load_pipeline import LoadPipeline


def main():

    ExtractPipeline().run()

    TransformPipeline().run()

    LoadPipeline().run()


if __name__ == "__main__":
    main()