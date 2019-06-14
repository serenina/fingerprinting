from fingerprinting.file_type import file_fingerprinting


class TestFileFingerprinting(object):
    def test_png_file_type(self, image_file):
        file_type = file_fingerprinting(image_file)
        assert file_type == 'PNG'

    def test_pdf_file_type(self, pdf_file):
        file_type = file_fingerprinting(pdf_file)
        assert file_type == 'PDF'

    def test_file_type_unkown(self, txt_file):
        file_type = file_fingerprinting(txt_file)
        assert file_type is None

    def test_file_not_found(self):
        file_type = file_fingerprinting('something.jpg')
        assert file_type is None
