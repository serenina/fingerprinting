import pytest
from PIL import Image
from fpdf import FPDF


@pytest.fixture()
def image_file(tmpdir):
    img = Image.new('RGB', (60, 30), color='red')
    p = tmpdir.mkdir("sub").join('img.png')
    img.save(str(p))
    return p


@pytest.fixture()
def pdf_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
    pdf.output(str(p))
    return p


@pytest.fixture()
def txt_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    return p
