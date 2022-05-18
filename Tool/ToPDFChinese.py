"""
@Author:张时贰
@Date:2022年04月25日
CSDN:张时贰
"""
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import reportlab.pdfbase.ttfonts

'''
https://blog.csdn.net/u014627536/article/details/104060211?ops_request_misc=&request_id=&biz_id=102&utm_term=%20try:%20%20%20%20%20%20%20%20%20reportlab.pdfbas&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~sobaiduweb~default-0-104060211.nonecase&spm=1018.2226.3001.4450
'''
# 创建水印信息
def create_watermark(content):
    """水印信息"""
    # 默认大小为21cm*29.7cm
    file_name = "mark.pdf"
    # 水印PDF页面大小
    c = canvas.Canvas ( file_name, pagesize=(30*cm, 30*cm) )
    # 移动坐标原点(坐标系左下为(0,0))
    c.translate ( 4*cm, 0*cm )
    # 设置字体格式与大小,中文需要加载能够显示中文的字体，否则就会乱码，注意字体路径
    try:
        reportlab.pdfbase.pdfmetrics.registerFont (
            reportlab.pdfbase.ttfonts.TTFont('yahei','C:\Windows\Fonts\STHUPO.TTF'))
        c.setFont ( 'yahei', 50 )
    except:
        # 默认字体，只能够显示英文
        c.setFont ( "Helvetica", 30 )
        content = "watermark"

    # 旋转角度度,坐标系被旋转
    c.rotate ( 30 )
    # 指定填充颜色
    c.setFillColorRGB ( 0, 0, 0 )
    # 设置透明度,1为不透明
    c.setFillAlpha ( 0.05 )
    # 画几个文本,注意坐标系旋转的影响
    c.drawString ( 0*cm, 3*cm, content )
    # 关闭并保存pdf文件
    c.save ()
    return file_name


# 插入水印
def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    pdf_output = PdfFileWriter ()
    input_stream = open ( pdf_file_in, 'rb' )
    pdf_input = PdfFileReader ( input_stream, strict=False )

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages ()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader ( open ( pdf_file_mark, 'rb' ), strict=False )
    # 给每一页打水印
    for i in range ( pageNum ):
        page = pdf_input.getPage ( i )
        page.mergePage ( pdf_watermark.getPage ( 0 ) )
        page.compressContentStreams ()  # 压缩内容
        pdf_output.addPage ( page )
    pdf_output.write ( open ( pdf_file_out, 'wb' ) )


if __name__ == '__main__':
    pdf_file_in = 'topdf.pdf'
    pdf_file_out = 'watermark.pdf'
    pdf_file_mark = create_watermark ( 'CSDN@张时贰' )
    add_watermark ( pdf_file_in, pdf_file_mark, pdf_file_out )