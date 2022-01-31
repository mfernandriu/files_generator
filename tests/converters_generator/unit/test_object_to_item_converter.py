from converters_generator.domain.object_to_item_converter_generator import ObjectToItemConverterGenerator
from tests.converters_generator.utils import class_file_contents_mother


def test_returns_converter_with_proper_file_name():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = ObjectToItemConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    converter_has_proper_file_name = converter.file_name == "example_to_item_converter.py"
    assert converter_has_proper_file_name


def test_returns_converter_with_proper_file_contents():
    class_file_contents = class_file_contents_mother.get_class_file_contents()
    converter_generator = ObjectToItemConverterGenerator()
    converter = converter_generator.generate(class_file_contents)
    expected_converter_file_contents = """def convert_many(example_list: List[Example]) -> List[ExampleItem]:
    return [convert(example) for example in example_list]


def convert(example: Example) -> ExampleItem:
    return ExampleItem(
        int_=example.int_,
        float_=example.float_,
        str_=example.str_,
        list_=example.list_,
    )"""
    converter_has_proper_file_contents = converter.file_contents == expected_converter_file_contents
    assert converter_has_proper_file_contents
