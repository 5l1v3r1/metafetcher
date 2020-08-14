import filetype
import fire
from PIL import Image
from PIL.ExifTags import TAGS
from rich.console import Console
from rich.table import Table
from PyPDF2 import PdfFileReader

image = ['png', 'jpg', 'tif', 'gif', 'jpx', 'bmp']
docs = ['doc', 'docx']
video = ['', '']
audio = ['', '']

def checkFileType(file):
    kind = filetype.guess(file)
    if kind is None:
        return 'None'
    else:
        return kind.extension

    
def main(file):
    global image
    global docs
    global audio
    global video

    table = Table()
    table.add_column("Device", style="cyan")
    table.add_column("Local Port", style="magenta")
    console = Console()
    filetype = checkFileType(file)
    if filetype == 'None':
        print()
    elif filetype in image:
        image = Image.open(file)
        # extract EXIF data
        exifdata = image.getexif()
        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            table.add_row(str(tag), str(data))
        console.print(table)
    elif filetype == 'pdf':
        table = Table()
        table.add_column("Device", style="cyan")
        table.add_column("Local Port", style="magenta")
        pdf = PdfFileReader(file)
        if pdf.isEncrypted:
            pdf.decrypt('')
        info = pdf.getDocumentInfo()
        table.add_row('Title', info.title)
        table.add_row('Subject', info.subject)
        table.add_row('Author', info.author)
        table.add_row('Creator', info.creator)
        table.add_row('Producer', info.producer)
        console.print(table)
    elif filetype in docs:
        print()
    elif filetype == 'zip':
        print()
    elif filetype == 'rar':
        print()
    elif filetype in video:
        print()
    elif filetype in audio:
        print()


if __name__ == '__main__':
    fire.Fire(main)
