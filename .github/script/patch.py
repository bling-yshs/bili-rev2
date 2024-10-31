import os
import glob
import subprocess

def find_file_with_pattern(pattern):
    # 在build文件夹中查找匹配模式的文件
    matches = glob.glob(os.path.join('./build', pattern))
    return matches[0] if matches else None

def main():
    try:
        # 切换到build目录
        os.chdir('./build')

        # 查找所需文件
        integrations_file = find_file_with_pattern('BiliRoamingX-integrations-*.apk')
        patches_file = find_file_with_pattern('BiliRoamingX-patches-*.jar')

        if not integrations_file or not patches_file:
            print("错误：未找到所需文件")
            return

        # 获取文件名（不含路径）
        integrations_name = os.path.basename(integrations_file)
        patches_name = os.path.basename(patches_file)

        # 构建命令
        command = [
            'java',
            '-jar',
            'revanced-cli.jar',
            'patch',
            '--merge',
            integrations_name,
            '--patch-bundle',
            patches_name,
            '--signing-levels',
            '1,2,3',
            'bili.apk'
        ]

        # 执行命令
        print("执行命令：", ' '.join(command))
        subprocess.run(command, check=True)

    except Exception as e:
        print(f"发生错误：{str(e)}")

if __name__ == "__main__":
    main()
