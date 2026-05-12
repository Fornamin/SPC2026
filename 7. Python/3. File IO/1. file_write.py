with open('7. Python/File/file.txt', 'a', encoding = 'UTF-8') as file:
    # Encoding 설정이 없으면 한글 꺠짐
    # 여기에 파일에 적을 내용을 입력
    file.write('데이터테스트\n')
    file.write('3element')