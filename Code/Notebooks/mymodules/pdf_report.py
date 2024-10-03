from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

class PDFReport:
    def __init__(self, name, fonts=None) -> None:
        self.pdf_name = name
        self.story = []
        self.doc = SimpleDocTemplate(self.pdf_name, pagesize=A4)
        self.styles = getSampleStyleSheet()  # 定義樣式表
        
        if fonts:
            self.font_create(fonts)
        else:
            self.fonts = [self.styles['BodyText']]  # 使用默認字體

    def image_pdf_wh(self, image_path):
        with PILImage.open(image_path) as img:
            img_width, img_height = img.size  # 圖片的寬度和高度（像素）

        max_width_inch = 7
        max_height_inch = 4
        
        aspect_ratio = img_width / img_height

        if img_width > img_height:
            display_width = min(max_width_inch, img_width / img_height * max_height_inch)
            display_height = display_width / aspect_ratio
        else:
            display_height = min(max_height_inch, img_height / img_width * max_width_inch)
            display_width = display_height * aspect_ratio

        return display_width, display_height
    
    def add_image(self, image_path):
        display_width, display_height = self.image_pdf_wh(image_path)
        img = Image(image_path, display_width * inch, display_height * inch)
        self.story.append(img)
        self.story.append(Spacer(1, 12))
    
    def add_title(self, title, font=0, font_size=16, alignment=TA_CENTER):
        if font_size:
            self.fonts[font].fontSize = font_size
        if alignment:
            self.fonts[font].alignment = alignment
        self.story.append(Paragraph(title, self.fonts[font]))
        self.story.append(Spacer(1, 12))

    def add_content(self, text_content, font=0, font_size=None, alignment=None):
        if font_size:
            self.fonts[font].fontSize = font_size
        if alignment:
            self.fonts[font].alignment = alignment
        self.story.append(Paragraph(text_content, self.fonts[font]))
        self.story.append(Spacer(1, 12))

    
    def font_create(self, fonts, font_sizes=None, alignments=None):
        self.fonts = []
        if font_sizes is None:
            font_sizes = [12] * len(fonts)  # 默認字體大小為12
        if alignments is None:
            alignments = [TA_LEFT] * len(fonts)  # 默認為左對齊

        for i in range(len(fonts)):
            fontname = f'font{i}'
            pdfmetrics.registerFont(TTFont(fontname, fonts[i]))
            style = ParagraphStyle(
                name=fontname,
                fontName=fontname,
                fontSize=font_sizes[i],  # 設置字體大小
                alignment=alignments[i],  # 設置對齊方式
                parent=self.styles["Normal"],
            )
            self.fonts.append(style)

    def create(self):
        self.doc.build(self.story)
        print(f"PDF報告已生成：{self.pdf_name}")
        
if __name__ == "__main__":
    export_pdf = True
    # fonts = [r"F:\Code\Digital-Image-Processing\Code\Resources\Fonts\Times New Roman.ttf", r"F:\Code\Digital-Image-Processing\Code\Resources\Fonts\kaiu.ttf"]
    fonts = [r"/Users/xieweizhe/Desktop/MacCode/Digital-Image-Processing/Code/Resources/Fonts/Times New Roman.ttf", r"/Users/xieweizhe/Desktop/MacCode/Digital-Image-Processing/Code/Resources/Fonts/kaiu.ttf"]
    pdf_content = [
        {'type':'title', 'add': 'Test Report', 'font':0}
        ]
    import os
    os.makedirs('outputs', exist_ok=True)
    pdfname = f"outputs/report.pdf"
    addcontent = [
        {'type':'content', 'add': "中文文字", 'font':1},
        {'type':'image', 'add': "/Users/xieweizhe/Desktop/MacCode/Digital-Image-Processing/Code/Resources/Data/cat.jpg", 'font':0},]
    pdf_content.extend(addcontent)
    
    report = PDFReport(name=pdfname, fonts=fonts)

    for content in pdf_content:
        if content.get('type') == 'title':
            report.add_title(content.get('add'), font=content.get('font'))
        elif content.get('type') == 'content':
            report.add_content(content.get('add'), font=content.get('font'))
        elif content.get('type') == 'image':
            report.add_image(content.get('add'))
        
    report.create()