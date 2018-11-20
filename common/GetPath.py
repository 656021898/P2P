# -*_ coding:utf-8 _*-

import os

class GetPath:

    @staticmethod
    def get_path():
        project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
        return project_path


if __name__ == "__main__":
    print(GetPath.get_path())