thumbnail_custom_size = "500xAAA"
thumb_size_list = thumbnail_custom_size.split("x")
if thumb_size_list[0].isdigit() is True and thumb_size_list[1].isdigit() is True:
    print('OK')
else:
    print('thumbnail_custom_size is not digit')
print(thumb_size_list)

