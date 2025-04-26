def main():
    print("Hello from personal-website!")


if __name__ == "__main__":
    main()
    import os

    def print_directory_structure(path):
        for root, dirs, files in os.walk(path):
            level = root.replace(path, '').count(os.sep)
            indent = '-' * 4 * (level)
            print(f'{indent}{os.path.basename(root)}/')
            sub_indent = '-' * 4 * (level + 1)
            for f in files:
                print(f'{sub_indent}{f}')

    # Укажите путь к вашему проекту
    project_path = r'C:\Users\ilyas\Documents\GitHub\personal_website\personal_website'
    print_directory_structure(project_path)