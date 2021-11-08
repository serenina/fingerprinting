from fingerprinting.file_type import file_fingerprinting
from click.testing import CliRunner

runner = CliRunner()


class TestFileFingerprinting(object):
    def test_png_file_type(self, image_file):
        result = runner.invoke(file_fingerprinting, ['--path', image_file.strpath])
        assert 'PNG' in result.output

    def test_pdf_file_type(self, pdf_file):
        result = runner.invoke(file_fingerprinting, ['--path', pdf_file.strpath])
        assert 'PDF' in result.output

    def test_file_type_unkown(self, txt_file):
        result = runner.invoke(file_fingerprinting, ['--path', txt_file.strpath])
        assert result.return_value is None

    def test_file_not_found(self):
        result = runner.invoke(file_fingerprinting, ['--path', 'something.jpg'])
        assert result.return_value is None
