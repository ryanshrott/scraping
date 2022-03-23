classes = ['platform_img win',
            'platform_img mac',
            'platform_img linux',
            'vr_supported']

def get_platforms(list_classes):
    platforms = []
    for item in list_classes:
        platform = item.split(' ')[-1]
        if platform == 'win':
            platforms.append('Windows')
        if platform == 'mac':
            platforms.append('Mac os')
        if platform == 'linux':
            platforms.append('Linux')
        if platform == 'vr_supported':
            platforms.append('Vr Supported')

    return platforms
print(get_platforms(classes))