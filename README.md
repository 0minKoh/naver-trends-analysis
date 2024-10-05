# How it Works

## 1. Naver Trends Excel 다운로드

1-1. [네이버 트렌드 키워드 검색](https://datalab.naver.com/keyword/trendSearch.naver) 에서 검색어 5개 입력, 기간을 2019.1.1 ~ 2024.10.4로 입력

1-2. '네이버 검색 데이터 조회' Btn 클릭
1-3. 페이지 로드가 완료되고, '다운로드' 버튼이 Clickable 상태가 되면 클릭하여 엑셀 다운로드

## 2. Naver Trends Excel에서 브랜드별 상대값 가져오기

2-1. 엑셀 파일이 모두 다운로드되면 read_excel로 가져오기

2-2. (index: 6) 7행부터 날짜, 브랜드, 날짜, 브랜드 ... 시작되므로, 5개 브랜드멸 상대값 가져오기

2-3. 다운로드된 excel 파일을 삭제

## 3. Column(naver_trends) 생성하기

3-1. 새로운 csv 파일을 `naver_search_data.csv` Write하여, Column을 생성 (naver_trends)
Row: 기간
Column: 상댓값

## 4. (없음)

## 5. Naver 검색광고 플랫폼에서 2024.9 절대 검색량 얻기

5-1. `naver_search_data.csv`에서 키워드별 상대 검색량을 가져옴

5-2. 5개 단위로 (네이버 트렌드에서 함께 검색된 그룹), 분리하고 각 그룹에서 1번째 키워드(브랜드명)에서 `브랜드명`, `2024.09의 검색량 평균`을 산출하여 Length가 5인 `keywords_relative_202409_list`(`List<Obj<브랜드명: 2024.09의 검색량 평균>>`)을 반환

5-2. List 내 요소들을 순회하며, `브랜드명`(key) 를 [키워드 검색 도구](https://manage.searchad.naver.com/customers/1261829/tool/keyword-planner)에서 검색

5-3. 최상단의 `월간검색수` 에서 `PC`, `모바일` 값을 더한 후 30으로 나누어 2024.09의 절대 검색량 평균을 산출, List 내의 2024.09의 상대 검색량 평균을 나눔

```
2024.09의 절대 검색량 평균 / 2024.09의 상대 검색량 평균 = 상대 검색량 1당 절대 검색량
```

## 6. 상대 검색량을 절대 검색량으로 변환

각 그룹 (5개)의 모든 키워들의 절대 검색량을 구한 뒤, 새로운 Column (절대 검색량)에 값 작성

## 7. 반복 (절대 검색량 Column에 값 생성)
