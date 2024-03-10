# 변수 초기화
userMessages = []
assistantMessages = []
myDateTime = ''

def start():
    global myDateTime
    date = input("생년월일을 입력해주세요 (YYYY-MM-DD): ")
    hour = input("시간을 입력해주세요 (HH:MM): ")
    if not date:
        print("생년월일을 입력해주세요.")
        return
    myDateTime = date + " " + hour
    print("채팅이 시작되었습니다!")

def send_message():
    global userMessages, assistantMessages, myDateTime
    message = input("메시지를 입력하세요: ")

    # 사용자 메시지 출력
    print(f"User: {message}")
    userMessages.append(message)

    # 백엔드 서버와의 통신 (이 Python 코드에서는 구현되지 않았습니다.)
    # 실제로는 HTTP 요청을 보내거나 데이터베이스와 연결하는 등의 작업이 필요합니다.
    # 이 부분은 프로젝트의 요구사항에 따라 추가 구현이 필요합니다.

    # 챗봇 메시지 출력 (이 Python 코드에서는 구현되지 않았습니다.)
    # 챗봇의 응답을 생성하는 로직도 추가로 구현해야 합니다.

# 예시 사용법
start()
send_message()
