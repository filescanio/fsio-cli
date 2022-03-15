from enum import Enum


class FileType(str, Enum):
    bits64 = '64bits'
    apk = 'apk'
    bat = 'bat'
    bmp = 'bmp'
    csv = 'csv'
    doc = 'doc'
    docm = 'docm'
    docx = 'docx'
    dot = 'dot'
    dotm = 'dotm'
    dotx = 'dotx'
    eml = 'eml'
    elf = 'elf'
    gif = 'gif'
    hta = 'hta'
    htm = 'htm'
    html = 'html'
    img = 'img'
    java = 'java'
    javabytecode = 'java-bytecode'
    javascript = 'javascript'
    jpg = 'jpg'
    lnk = 'lnk'
    mbox = 'mbox'
    mhtml = 'mthml'
    msg = 'msg'
    msi = 'msi'
    mso = 'mso'
    ole = 'ole'
    pdf = 'pdf'
    pedll = 'pedll'
    peexe = 'peexe'
    png = 'png'
    ppt = 'ppt'
    pptm = 'pptm'
    pptx = 'pptx'
    pot = 'pot'
    potm = 'potm'
    potx = 'potx'
    ps = 'ps'
    pub = 'pub'
    powershell = 'powershell'
    rfc822 = 'rfc822'
    rtf = 'rtf'
    svg = 'svg'
    txt = 'txt'
    vbs = 'vbs'
    wsf = 'wsf'
    xls = 'xls'
    xlsm = 'xlsm'
    xlsb = 'xlsb'
    xlsx = 'xlsx'
    xlt = 'xlt'
    xltm = 'xltm'
    xltx = 'xltx'
    xsl = 'xsl'


file_categories = {
    'pdf': ['pdf'],
    'pe': ['peexe', '64bits'],
    'elf': ['elf'],
    'eml': ['rfc822', 'msg', 'eml'],
    'office': [
        'doc', 'docm', 'docx', 'dot', 'dotm', 'dotx',
        'ole', 'ppt', 'pptm', 'pptx', 'pot', 'potm', 'potx',
        'rtf', 'xls', 'xlsb', 'xlsm', 'xlsx', 'xlt', 'xltm', 'xltx',
        'xsl', 'csv'
    ],
    'mbox': ['mbox'],
    'lnk': ['lnk']
}
