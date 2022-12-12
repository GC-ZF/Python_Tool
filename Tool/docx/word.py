"""
@Author:张时贰
@Date:2022年12月12日
@CSDN:张时贰
@Blog:zhangshier.vip
"""
'''
1，Document对象，表示一个word文档。
2，Paragraph对象，表示word文档中的一个段落
3，Paragraph对象的text属性，表示段落中的文本内容。
'''
import os
import docx


def get_file(rule, path_before):
    tmp = [ ]
    for root, dirs, fs in os.walk ( path_before ):
        for f in fs:
            if f.endswith ( rule ):  # 判断结尾
                tmp.append ( f )
    return tmp


def alter_file(path_before, path_after, doc_list):
    for f in doc_list:
        # 获取文档对象
        file = docx.Document ( path_before + '/' + f )
        '''
            获取段落内容
            主要方法：
                file.paragraphs 段落数
                file.paragraphs[i].text 段落内容
        '''
        # print ( "段落数:" + str ( len ( file.paragraphs ) ) )  # 每个回车隔离一段
        # # 输出每一段的内容
        # for para in file.paragraphs:
        #     print ( para.text )
        #
        # # 输出段落编号及段落内容
        # for i in range ( len ( file.paragraphs ) ):
        #     print ( file.paragraphs[ i ].text )

        '''
            读取表格数据
            主要方法：
                document.tables 表格对象 list类型
                table.cell(i,j).text    行列内容
                table.rows  行数
        '''
        tables = file.tables  # 获取文件中的表格集
        table = tables[ 0 ]  # 获取文件中的第一个表格
        # print ( table.cell ( 0, 1 ).text )
        # print ( table.cell ( 1, 1 ).text )
        '''
            修改表格内容
            table.cell(1,1).paragraphs[0].runs[0]
        '''
        name = table.cell ( 0, 1 ).paragraphs[ 0 ].runs
        name[ 0 ].text = '英子钓大鱼'
        sex = table.cell ( 1, 1 ).paragraphs[ 0 ].runs
        sex[ 0 ].text = '女'
        file.save ( path_after + '/' + f )


if __name__ == "__main__":
    path_before = './处理前'  # 需要处理的文件夹路径
    path_after = './处理后'
    rule = '.docx'  # 后缀
    doc_list = get_file ( rule, path_before )  # 扫描该路径下所有文件

    print ( "需要处理的文件 ", doc_list )

    alter_file ( path_before, path_after, doc_list )

    print ( '处理完成' )
