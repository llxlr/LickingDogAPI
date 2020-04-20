def read_log(path):
    """读取日志信息,pv:调用数,uv:用户数,ts:浏览量"""
    pv = uv = ts = 0
    with open(path, 'r', encoding='gbk') as f:
        for i in f.readlines():
            if 'pv' in i:
                pv += 1
            elif 'uv' in i:
                uv += 1
            elif 'ts' in i:
                ts += 1
        return {'pv': pv, 'uv': uv, 'ts': ts}
