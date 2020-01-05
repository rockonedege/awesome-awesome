entries = """
https://github.com/vuejs/awesome-vue
https://github.com/vinta/awesome-python
https://github.com/veggiemonk/awesome-docker
https://github.com/josephmisiti/awesome-machine-learning
https://github.com/Hack-with-Github/Awesome-Hacking
https://github.com/wasabeef/awesome-android-ui
https://github.com/sindresorhus/awesome-nodejs
https://github.com/fffaraz/awesome-cpp
https://github.com/rigtorp/awesome-modern-cpp
https://github.com/justjavac/awesome-wechat-weapp
https://github.com/sorrycc/awesome-javascript
https://github.com/binhnguyennus/awesome-scalability
https://github.com/awesome-selfhosted/awesome-selfhosted
https://github.com/jobbole/awesome-python-cn
https://github.com/bayandin/awesome-awesomeness
https://github.com/facert/awesome-spider
https://github.com/fenbf/AwesomePerfCpp

"""

def to_list(entries):
    items = []
    for e in set(entries.split('\n')):
        if e:
            title = e.rsplit('/')[-1].capitalize()
            items.append(f'- [{title}]({e})')

    return '\n'.join(sorted(items))

def main():
    from pathlib import Path

    text = """
# awesome-awesome
An Awesome-* lists of **personal** interests.

""" + to_list(entries)

    readme = Path(__file__).absolute().parent/'README.md'
    readme.write_text(text, encoding='utf-8')
    print('Done.')

if __name__ == "__main__":
    main()
