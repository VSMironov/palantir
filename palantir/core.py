import helpers


def get_camera_picture():
    camera_list = helpers.get_camera_list()
    for camera_link_id, link in camera_list:
        img = helpers.get_picture(link)
        helpers.db_write_picture(camera_link_id, img)


if __name__ == '__main__':
    get_camera_picture()
