# How to create

1.

[이 프로젝트](https://github.com/haklee/boj-i-solved)를 활용하여 `solved_problems.json` 파일을 만들고, 현재 프로젝트의 루트 경로에 둔다.

2.

다음의 명령어로 솔루션 폴더를 업데이트 한다.

``` python
python create_files.py
```

3.

다음의 명령어로 README.md 파일을 업데이트 한다.

``` python
python build_readme.py
```

# How to update

1.

한 문제에 같은 언어로 여러 번 풀이를 제출했을 수 있고, 앞의 과정을 통해 생성된 폴더에는 이 풀이들에 대한 파일이 각각 비어있는 상태로 생성되어 있을 것이다.

우선은 원하는 풀이를 직접 파일에 옮긴 다음에 업데이트가 완료된 문제를 `skip_list.json`에 추가하자. 해당 파일은 아래와 같은 포맷으로 되어있으며, 문제 번호는 문자열이 아닌 정수를 사용한다.

```json
{
    "skip_problems": [
        1000,
        1001,
        ...
    ]
} 
```

2.

다시 `How to create`의 `create_files`, `build_readme` 과정을 진행한다.
