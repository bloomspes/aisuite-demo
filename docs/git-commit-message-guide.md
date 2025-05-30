# Git 커밋 메시지 가이드

이 가이드는 다음 자료를 바탕으로 작성되었습니다.

- <https://github.com/agis/git-style-guide>
- <https://cbea.ms/git-commit/>

## 핵심 원칙

1. 커밋 메시지는 명령형으로 작성합니다.
   예: "기능 추가", "버그 수정" 등과 같이 커밋이 적용될 때 어떤 작업을
   수행하는지 명확하게 표현합니다.
2. 단순한 변경사항 나열보다는 변경의 의도, 핵심 목적, 주의사항에 중점을
   두고 작성합니다.
3. 커밋 메시지의 제목(요약)은 50자 이내로 작성하여 로그에서 빠르게 내용을
   파악할 수 있게 합니다.
4. 본문은 한 줄에 72자를 넘지 않도록 하고, 각 문장은 별도의 줄에 작성하여
   가독성과 일관성을 높입니다.
5. 본문에서는 불릿 포인트나 목록 형식을 피하고, 완전한 문장과 문단으로
   연결된 설명을 작성합니다.
6. 모든 커밋 메시지는 한국어로 작성하여 일관성을 유지하고 모든 협업자가
   이해할 수 있게 합니다.

## 글자 수 참고

```txt
|----+----1----+----2----+----3----+----4----+----5|
요약은 이 줄(50자)을 넘지 않게 작성합니다.

|----+----1----+----2----+----3----+----4----+----5----+----6----+----7|
본문은 이 줄(72자)을 넘지 않게 작성합니다.
```

## 메시지 구조

```txt
[요약] - 최대 50자, 명령형 사용

[첫 번째 단락] - 각 문장은 줄바꿈으로 구분합니다.
하나의 완결된 생각은 별도의 줄에 작성합니다.
이렇게 하면 로그 히스토리에서 메시지를 더 쉽게 읽을 수 있습니다.
변경된 '무엇'이 아니라 '왜' 변경했는지에 초점을 맞춥니다.

[추가 단락] - 빈 줄로 구분합니다.
각 단락은 변경사항의 서로 다른 측면을 설명합니다.
```

## 줄 길이 규칙

본문의 모든 줄은 72자를 초과하지 않아야 합니다.
이 규칙은 영어와 한국어 모두 동일하게 적용됩니다.
커밋 전에 반드시 줄 길이를 확인하고, 한 줄이라도 72자를 넘으면 전체
메시지를 다시 작성해야 합니다.
이 규칙은 예외 없이 엄격하게 지켜져야 합니다.

## 예시

```txt
헬스 체크 API 추가 및 문서 업데이트

서비스 상태 모니터링을 위한 새로운 헬스 체크 API 엔드포인트 구현.
외부 시스템에서 서비스 작동 상태 확인 가능하도록 함.
엔드포인트는 정상 상태일 때 HTTP 200, 비정상일 때 503 반환.

새 엔드포인트 사용법 설명하는 문서 업데이트.
일반적인 모니터링 시나리오와 통합 패턴에 대한 예제 추가.
발생 가능한 구성 문제에 대한 문제 해결 가이드 포함.
```