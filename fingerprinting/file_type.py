import click
import logging

signatures = {'PK': 'Microsft Office Document',
              'JFIF': 'JPEG',
              'GIF': 'GIF',
              'BPS': 'PSD',
              'PNG': 'PNG',
              'II': 'TIFF',
              'BM': 'BMP',
              'PDF': 'PDF',
              }

logging.basicConfig(
    format='[%(levelname)s] %(message)s',
    level=logging.INFO
)
logger = logging.getLogger('file_fingerprinting')


@click.command()
@click.option('--path', type=str, default=None, help='local directory to the file')
def file_fingerprinting(path):
    try:
        logger.log(logging.INFO, 'Reading file')
        with open(path, 'rb') as f:
            first_bytes = f.read(100)
            for key in signatures.keys():
                if key in str(first_bytes):
                    click.echo(f'File extension: {signatures[key]}')
                else:
                    continue
            return None
    except FileNotFoundError:
        logger.log(logging.ERROR, 'FileNotFoundError')
        pass


if __name__ == '__main__':
    file_fingerprinting()
