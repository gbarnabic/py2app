import os
def check(cmd, mf):
    m = mf.findNode('matplotlib')
    if m is None or m.filename is None:
        return None

    return dict(
        prescripts=['py2app.recipes.matplotlib_prescript'],
        resources=[os.path.join(os.path.dirname(m.filename), 'mpl-data')],
    )

    return None

    # XXX: unclear why this is needed and according
    # to mail on pythonmac-sig this breaks with
    # current versions of matplatlib and pytz.
    #mf.import_hook('pytz.zoneinfo', m, ['UTC'])
    return dict(
        packages = ['matplotlib']
    )
